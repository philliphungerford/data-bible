tags:: #code/r

- ```
  # set the environment variable
  Sys.setenv(
    INSTANCE_DEV = "UNCISQL-D01MDB.nswhealth.net\\DW_DEV",
    INSTANCE_UAT = "UNCISQL-U01MDB.nswhealth.net\\DW_UAT",
    INSTANCE_PRD = "SVCISQL-P02MDB.nswhealth.net\\REPORTING_PROD"
  )
  
  # use the variable
  InstanceDev         <- Sys.getenv("INSTANCE_DEV")
  InstanceUAT         <- Sys.getenv("INSTANCE_UAT")
  InstancePRD         <- Sys.getenv("InstancePRD")
  ```