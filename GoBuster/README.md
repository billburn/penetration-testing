# GoBuster Command Usage

## Bypass the Wildcard Error message
```
gobuster dir -u <url-goes-here> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 40 -k --wildcard -s "200,204,301,302"
```

## Define Bad HTTP Code
```
gobuster dir -u http://10.129.81.81:8080 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt --wildcard -s "200,204,301,302,307,401,403" -b 403
```