tags:: #code/r

- ```
  library(DBI)
  copy_new_rows_by_key <- function(
      source_conn,
      target_conn,
      source_table,
      target_table,
      key_column = "NotificationId"
  ) {
    message(sprintf("Syncing rows from '%s' to '%s' using key column '%s'...", 
                    source_table, target_table, key_column))
    
    # Step 1: Get key values from target DB
    target_query <- sprintf("SELECT %s FROM %s", key_column, target_table)
    target_keys <- dbGetQuery(target_conn, target_query)[[key_column]]
    
    # Step 2: Build query to get new rows from source DB
    if (length(target_keys) == 0) {
      source_query <- sprintf("SELECT * FROM %s", source_table)
    } else {
      key_list <- paste(shQuote(target_keys), collapse = ",")
      source_query <- sprintf(
        "SELECT * FROM %s WHERE %s NOT IN (%s)", 
        source_table, key_column, key_list
      )
    }
    
    new_rows <- dbGetQuery(source_conn, source_query)
    
    # Step 3: Write new rows to target table
    if (nrow(new_rows) > 0) {
      dbWriteTable(target_conn, target_table, new_rows, append = TRUE, row.names = FALSE)
      message(sprintf("Copied %d new rows to '%s'.", nrow(new_rows), target_table))
    } else {
      message("No new rows to copy.")
    }
  }
  
  ```
-