import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# CONNECT
#-------------------------------------------------------------------------------
# Define the ODBC connection string
conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=serverdev,50000;"
    "DATABASE=dbname;"
    "Trusted_Connection=yes;"  # Or use UID and PWD if needed
    "Encrypt=no;"              # Optional, depending on your server config
)

# pyodbc connection (for general use)
conn = pyodbc.connect(conn_str)

# READ
#-------------------------------------------------------------------------------
df = pd.read_sql("SELECT * FROM your_table_name", conn)

# Close connection when done
conn.close()

# WRITE
#-------------------------------------------------------------------------------
# Create SQLAlchemy engine for pandas `.to_sql()` support
engine = create_engine(
    "mssql+pyodbc:///?odbc_connect=" + pyodbc.connect(conn_str).getdsn()
)

# Example DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
}
df_to_write = pd.DataFrame(data)

# Write to SQL Server (append or replace as needed)
df_to_write.to_sql('your_new_table_name', engine, if_exists='replace', index=False)
