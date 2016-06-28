# IndexFolders
Convert folders to SQL

## Find out number of files per drive
select drive, count(id) from 
	(select id, substr(folder, 1, 3) as drive from file) 
group by drive 

## Search for PDF files in a specific drive
select * from file 
where substr(folder,1,3) = 'x:\' and type = '.pdf' 

## Get full path names
select id, (folder || '\' || name || type), created, modified, accessed, size 
from file 
