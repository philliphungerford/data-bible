tags:: #code/r

- ```
  load_or_install <- function(...){
    packages <- unlist(list(...))
    for (pkg in packages) {
      if (!require(pkg, character.only = TRUE)) {
        message(sprintf("Package '%s' not found. Installing now...", pkg))
        install.packages(pkg, dependencies = TRUE)
        library(pkg, character.only = TRUE)
      } else {
        message(sprintf("Package '%s' loaded successfully.", pkg))
      }
    }
  }
  load_or_install("tidyverse", "DBI", "odbc")
  ```