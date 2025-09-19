tags:: #code/r

- ```
  library(officer)
  library(tidyverse)
  
  convert_word_to_logseq <- function(docx_path, output_folder) {
    # Read Word doc
    doc <- read_docx(docx_path)
    
    # Extract paragraphs
    content <- docx_summary(doc) %>%
      filter(content_type == "paragraph") %>%
      pull(text)
    
    # Initialize storage
    current_date <- NULL
    notes_list <- list()
    
    for (line in content) {
      # Detect date headings (YYYY-MM-DD)
      if (grepl("^\\d{4}-\\d{2}-\\d{2}$", line)) {
        current_date <- line
        notes_list[[current_date]] <- c()
      } else if (!is.null(current_date)) {
        # Append note lines to the current date
        notes_list[[current_date]] <- c(notes_list[[current_date]], line)
      }
    }
    
    # Write to markdown files
    for (date in names(notes_list)) {
      file_path <- file.path(output_folder, paste0(date, ".md"))
      write_lines(notes_list[[date]], file_path)
      message("Wrote: ", file_path)
    }
  }
  
  # Example usage:
  convert_word_to_logseq("_LOG.docx", "journals")
  
  ```