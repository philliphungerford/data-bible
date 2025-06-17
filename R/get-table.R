library(tidyverse)

con <- DBI::dbConnect(
    odbc::odbc(),
    Driver   = "SQL Server",
    Port     = 50000,
    Server   = "SVCINCR-U01MDB.nswhealth.net\\NSWCR_PREPROD",
    Database = "NSWCREPathStaging",
    UID      = UID, # for sql auth
    PWD      = PWD, # for sql auth
    Encrypt = "yes",
    TrustServerCertificate = "yes" # for windows auth
)

Notifications <- tbl(con, "ImportNotification") %>% collect()