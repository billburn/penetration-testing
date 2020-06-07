# Impacket Tools

## Impacket SMBServer
```
$python3 impacket-smbserver -u <username> -p <password> <name of share> <location of share>
$python3 impacket-smbserver -smb2support -u <username> -p <password> <name of share> <location of share>
Sample Usage: $python3 impacket-smbserver -u myusername -p secretpassword myshare $(pwd)
Tip: use $(pwd) for the current working  directory
```

## MSSQL Client
```
$python3 mssqlclient.py -port 1433 -db volume -windows-auth <username>@<ip address>
```

## WMIExec
```
$python3 wmiexec.py <username@hostname>
$python3 wmiexec.py <username:password@hostname>
```

## LookupSID
```
$python3 lookupsid.py <domain/username@hostname>
$python3 lookupsid.py <domain/username:password@hostname>
```