
[Markup Language](https://www.markdownguide.org/cheat-sheet/)

- List nested files with extension  
`find . -type f -name '*.<c>'`

- List nested files with either extensions  
`find . -type f \( -name '*.<c>' -o -name '*.<pyd>' \)` 

- List files in some directory  
`find <dir_path/>  -type f -name '*.<pyx>' ` 

- Remove nested files with either extension     
`find . -type f \( -name '*.<c>'  -o -name '*.<pyd>' \) -exec rm {} \; ` 

- Remove nested files in some directory with extension  
`find <dir_path/> -type f \( -name '*.<c>'  -o -name '*.<pyd>' \) -exec rm {} \;`

- Rename files (.pyx -> .py) in some directory in with extension    
`find <dir_path> -type f -name '*.<pyx>' -exec bash -c 'mv "$0" "${0%.<pyx>}.<py>"' {} \;`





