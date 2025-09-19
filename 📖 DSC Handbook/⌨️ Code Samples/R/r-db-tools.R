library(DBI)
library(odbc)
library(tidyverse)

# CONNECT
#-------------------------------------------------------------------------------
con <- DBI::dbConnect(
    odbc::odbc(),
    Driver   = "SQL Server",
    Port     = 50000,
    Server   = "SVCINCR-U01MDB.nswhealth.net\\NSWCR_PREPROD",
    Database = "NSWCREPathStaging",
    UID      = "uid", # for sql auth
    PWD      = "pwd", # for sql auth
    Encrypt = "yes",
    TrustServerCertificate = "yes" # for windows auth
)

# READ
#-------------------------------------------------------------------------------
Notifications <- tbl(con, "ImportNotification") %>% collect()

# WRITE
#-------------------------------------------------------------------------------
DBI::dbWriteTable(con, "Notifications", new_rows, append = TRUE, row.names = FALSE)
