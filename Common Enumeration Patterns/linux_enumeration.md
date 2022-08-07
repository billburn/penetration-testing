# Linux Enumeration

| Command | Summary |
| ---------------------------- | ---------------------------- |
| placeholder | This is placeholder text |


| Check | Description |
| ---------------------------- | ---------------------------- |
| Sudo Local Privilege Escalation (CVE-2019-14287) | Sudo versions < 1.8.27 may be vulnerable to LPE, check: ```sudo -u#-1 /bin/bash``` |
| Sudo Buffer Overflow (CVE-2019-18634)| Sudo versions < 1.8.26 may be vulnerable to a buffer overflow, pwfeedback enabled: [GitHub for Code](https://github.com/saleemrashid/sudo-cve-2019-18634/blob/master/exploit.c) |