# GoBuster Command Usage

## Bypass the Wildcard Error message
```
gobuster dir -u <url-goes-here> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 40 -k --wildcard -s "200,204,301,302"
```