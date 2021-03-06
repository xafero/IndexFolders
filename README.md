# IndexFolders
Convert folders to SQL

## Examples

### Find out number of files per drive
```sql
select drive, count(id) from 
	(select id, substr(folder, 1, 3) as drive from file) 
group by drive 
```

### Search for PDF files in a specific drive
```sql
select * from file 
where substr(folder,1,3) = "x:\" and type = ".pdf" 
```

### Get full path names
```sql
select id, (folder || "\" || name || type), created, modified, accessed, size 
from file 
```

### Find out unique file extensions
```sql
select distinct substr(type,1,4) from file order by type asc
```
