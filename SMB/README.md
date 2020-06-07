# SMB Tools

## CrackMapExec
[URL] (https://github.com/byt3bl33d3r/CrackMapExec)
```
[Enumerated SMB Shares] $crackmapexec smb <ip address> --shares -u <username> -p <password>
[Password Spary User List and Password] $crackmapexec smb <ip address> -u <users.lst> -p <password> --continue-on-success
```

## SmbClient
```
[Enumerate SMB Shares - NULL Sessio] $smbclient -L //<ipaddress>
```

## SmbMap
[URL] (https://github.com/ShawnDEvans/smbmap)
```
[Enumerate SMB Shares - NULL Session] $smbmap -H <ip address> -u <username>
```

## Mount SMB to Linux Filesystem
```
NOTE: May need to install cifs-utils (sudo apt install cifs-utils)
1) mkdir /mnt/<sharename>
2) sudo mount -t cifs //<ipaddress>/<sharename> /mnt/<sharename>
```

## Mount SMB to Linux Filesystem (with creds)
```
1) mkdir /mnt/<sharename>
2) sudo mount -t cifs -o 'username=<username>,password=<password>' //<ip address>/sharename /mnt/<sharename>
```