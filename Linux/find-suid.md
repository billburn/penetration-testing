# Finding SUID / SGID Binaries

## SUID
```
find / -perm -4000 -exec ls -lah {} \; 2>/dev/null
```

## SGID
```
find / -perm -2000 -exec ls -lah {} \; 2>/dev/null
```