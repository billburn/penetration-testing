# Linux Enumeration Tips

## Grep all file for string
```
grep -ilR "flag11" / 2>/dev/null
```

## Remove all newline space from file 
```
tr -d "\n\r" < yourfile.txt
```

## Remove specific character or space from Nano
```
ctrl + \
search the file _char
replace the file _char
choose option
```

## Find SUID Files
```
find / -perm -u=s -type f 2>/dev/null
```

