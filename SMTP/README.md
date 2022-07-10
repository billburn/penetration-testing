# Enumerating SMTP

## smtp-user-enum

[URL] http://pentestmonkey.net/tools/smtp-user-enum
- Can test multiple methods: EXPN, VRFY, or RCPT (default is VRFY)

```
smtp-user-enum -M RCPT -U usernames.txt -t 10.129.1.151 -w 1 -D megabank.com -m 20 
```

## Sending Email CLI
```
sendemail -t nico@megabank.com -f badguy@ph0enix.local -s reel.htb.local -u Important -a invoice.rtf
```