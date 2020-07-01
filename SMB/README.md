# SMB Tools

## SmbClient
```
[Enumerate SMB Shares - NULL Session] $smbclient -L //<ipaddress>
[Enumerate SMB Shares as Users] $smbclient -L //<ipaddress> -U <username> (when prompted enter pass)
[Enumerate SMB Shares - NULL Session] $smbclient -U '' -N -L //<ipaddress>
[Connect to SMB Share] $smbclient //<ipaddress>/<sharename> -U <username>
```

## SmbMap
[URL] (https://github.com/ShawnDEvans/smbmap)
```
[Enumerate SMB Shares - NULL Session] $smbmap -H <ip address> -u <username>
```

## RPCClient
```
[NULL Session] $ rpcclient <ipaddress>
[NULL Session] $ rpcclient -U '' <ipaddress>
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

## NOTES ABOUT MS17-010
```
[URL] https://www.sevenlayers.com/index.php/146-unable-to-find-accessible-named-pipe
Essentially, sometimes you just need a set of creds to launch this attack - see write-up
```