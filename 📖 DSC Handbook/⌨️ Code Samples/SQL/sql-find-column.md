
```sql

USE YourDatabaseName;
GO

SELECT 
    t.name AS TableName,
    c.name AS ColumnName,
    ty.name AS DataType
FROM 
    sys.tables t
INNER JOIN 
    sys.columns c ON t.object_id = c.object_id
INNER JOIN
    sys.types ty ON c.user_type_id = ty.user_type_id
WHERE 
    c.name LIKE '%ColName%'  -- Change this to the column name you're searching for eg if you are looking for column 'PersonID'
ORDER BY 
    t.name;

```