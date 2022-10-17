# CrackMapExec
[URL] (https://github.com/byt3bl33d3r/CrackMapExec)

## Enumerate SMB Shares
```
[Enumerated SMB Shares] $crackmapexec smb <ip address> --shares -u <username> -p <password>
[Enumerated SMB Shares (alternative)] $crackmapexec smb <ip address> --shares -u <username> -p '<password>'
```

## SMB with Spider_Plus module
```
[First, identify the shares] $crackmapexec smb <ip address> -u <username> -p <password> --shares
[Spider the shares] $crackmapexec smb <ip address> -u <username> -p <password> -M spider_plus 'share_name' 
```

## SMB Users
```
crackmapexec smb <target> --users
crackmapexec smb <target> -u username -p password --users
```

## SMB Groups
```
crackmapexec smb <target> -u <username> -p <password> --groups
```

## SMB Loggedon Users
```
crackmapexec smb <target> -u <username> -p <password> --loggedon-users
```

## Enumerate Password Policy
```
[Password Policy] $crackmapexec smb --pass-pol <ipaddress>
```

## Password Spray Users
```
[Password Spray User List and Password] $crackmapexec smb <ip address> -u <users.lst> -p <password> --continue-on-success
```

## Null Session
```
crackmapexec smb <target(s)> -u '' -p ''
```

## Pass the Hash
```
crackmapexec smb <target(s)> -u username -H LMHASH:NTHASH
crackmapexec smb <target(s)> -u username -H NTHASH
