# Linux Enumeration Tips

## Default Ubuntu File Permissions
```
* Folders should be 0755
* Files shuld be 0664
find /home/user -type d -print0 | xargs -0 chmod 0775
find /home/user -type f -print0 | xargs -0 chmod 0664
```

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

## CAT not working
```
Have you tried less?
```
