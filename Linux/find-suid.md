# Finding SUID / SGID Binaries

## SUID
```
find / -perm -4000 -exec ls -lah {} \; 2>/dev/null
```

## SUID with -user flag
```
find / -user root -perm -4000 -exec ls -lah {} \; 2>/dev/null |grep "/bin"
```

## SGID
```
find / -perm -2000 -exec ls -lah {} \; 2>/dev/null
```