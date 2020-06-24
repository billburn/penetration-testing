# Impacket Tools

## Impacket SMBServer
```
$sudo python3 impacket-smbserver -u <username> -p <password> <name of share> <location of share>
$sudo python3 impacket-smbserver -smb2support -u <username> -p <password> <name of share> <location of share>
$sudo impacket-smbserver -smb2support <name of share> `pwd`

Sample Usage: $python3 impacket-smbserver -u myusername -p secretpassword myshare $(pwd)
Tip: use $(pwd) for the current working  directory
```

## PSExec
```
$python3 psexec.py username@<ip address>
Sample Usage: $python3 psexec.py Administrator@10.10.10.10 (enter password when prompted)
```

## MSSQLClient
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