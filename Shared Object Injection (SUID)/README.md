# Shared Object Injection

## Search for SUID files
```
find / -type f -perm -04000 -ls 2>/dev/null
```

## Use STRACE to search for missing files
```
strace /usr/local/bin/suid-so 2>&1 | grep -i -E "open|access|no such file"
...TRUNCATED
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/libc.so.6", O_RDONLY)        = 3
open("/home/user/.config/libcalc.so", O_RDONLY) = 3
```