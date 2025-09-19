tags:: #code/r

- ```
  import_sas_files <- function(folder_path, import = TRUE) {
    if (!requireNamespace("haven", quietly = TRUE)) {
      stop("The 'haven' package is required but not installed. Install it with install.packages('haven')")
    }
    
    sas_files <- list.files(path = folder_path, pattern = "\\.sas7bdat$", full.names = TRUE)
    
    if (length(sas_files) == 0) {
      warning("No SAS files found in the specified folder.")
      return(character(0))
    }
    
    cat("SAS files found:\n")
    print(sas_files)
    
    if (!import) {
      return(sas_files)
    }
    
    for (file in sas_files) {
      df_name <- make.names(tools::file_path_sans_ext(basename(file)))
      message(sprintf("Importing: %s as %s", basename(file), df_name))
      assign(df_name, haven::read_sas(file), envir = .GlobalEnv)
    }
    
    return(sas_files)
  }
  
  
  filenames <- import_sas_files("S:/Source Data/Master Linked Data/2020-45-06-CR2022/DataForUse", import=FALSE)
  
  for(i in basename(filenames)){print(i)}
  
  ```