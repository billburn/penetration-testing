# Powershell AD Module and PowerView Commands

## Bypassing PowerShell Security with Invishell
```
C:\InviShell\RunWithPathAsAdmin.bat (with admin)
C:\InviShell\RunWithRegistryNonAdmin.bat (without admin)
```

## Importing PowerShell Manually
```
Import-Module Microsoft.ActiveDirectory.Management.dll
Import-Module ActiveDirectory.psd1
```

## Get Current AD Domain
```
$ADClass = [System.DirectoryServices.ActiveDirectory.Domain]
$ADClass::GetCurrentDomain()
```

## Check Languge Contrained Mode
There are three modes:
- NoLanguage
- FullLanguage
- ConstrainedLanguage

```
$ExecutionContext.SessionState.LanguageMode
```

## Active Directory Domain Enumeration

| PowerView | Description |
| ---------------------------- | ---------------------------- |
| Get-NetDomain | Gets domain information |
| Get-NetDomain -Domain domain.local | Gets specific domain information |
| Get-DomainSid | Gets the SID for the current domain |
| Get-DomainPolicyData | Gets AD Domain Policy |
| Get-DomainPolicyData -domain domain.local | Gets AD Doamin Password Policy | 
| (Get-DomainPolicyData).systemaccess | PowerView prettified version of the domain policy |
| (Get-DomainPolicyData).kerberospolicy | PowerView prettified version of the kerberos policy |
| Get-DomainController | Gets information about the domain controller(s) |
| Get-DomainController -Domain domain.local | Gets domain controller(s) for another domain |
| Get-DomainUser * | Gets information about all AD users |
| Get-DomainUser -Identity username | Gets information about a single AD user |
| Get-DomainUser -Identity username -Properties * | Gets all properties for all users in the domain |
| Get-DomainUser -LdapFilter "Description=\*Built\*" \| Select name, description | Search domain users with specific attributes |
| Get-DomainUser -SPN -Properties samaccountname,serviceprincipalname | Finds all Kerberoastable users |
| Get-NetUser \| select samaccountname, description, pwdlastset | PowerView example to filter domain users by properties |
| Get-NetUser -properties name, pwdlastset, etc... | Another example of filtering properties |
| Get-NetUser -properties name, description |Check description field for passwords |
| Get-DomainComputer \| select Name | Gets a list of computers in the domain |
| Get-DomainComputer -OperatingSystem "\*Server 2016\*" | Gets a list of computers in the domain running Server 2016 |
| Get-DomainGroup \| select Name | Get all the groups in the current domain |
| Get-DomainGroup -Domain domain.local \| select Name | Get all group propertues in the current domain |
| Get-DomainGroup \*admin\* | Get all groups containing the word "admin" | 
| Get-DomainGroupMember -Identity "Domain Admins" -Recurse | Get all members of the Domain Admins Group |
| Get-DomainGroup -UserName "username" | Get the group membership for \<username\> |
| Get-NetLocalGroup -ComputerName dcorp-dc -ListGroups | Lists all the local groups (needs admin privs on non-dc machines) |
| Get-NetLocalGroup -ComputerName dcorp-dc -Recurse | Lists members of all local groups (needs admin privs on non-dc machines) |
| Get-NetLocalGroup -ComputerName dcorp-dc -GroupName Administrators| Lists members of "Administratprs" group (needs admin privs on non-dc machines) |
| Get-NetLoggedOn -ComputerName \<computer name\> | Gets logged on users on a computer (needs local admin privs on target) |
| Get-LoggedOnLocal -ComputerName \<computer name\> | Gets locally logged on users on a computer (needs local admin privs on target) |
| Get-LastLoggedOn -ComputerName \<computer name\> | Gets last logged on user on a computer (needs local admin privs on target) |
| Invoke-ShareFinder -Verbose | Find shares on hosts in current domain |
| Invoke-FileFinder -Verbose | Find sensitive files on computers in the domain |
| Get-NetFileServer | Get all fileserver in the domain | 
| Get-DomainGPO | Lists all the GPOs in the current domain | 
| Get-DomainGPO -ComputerIdentity \<computer name\> | Lists all the GPOs for the specific computer |
| Get-DomainGPOLocalGroup | Lists GPO(s) which use restricted groups ir groups.xml |
| Get-DomainGPOComputerLocalGroupMapping -ComputerIdentity \<computer name\> | Gets users which are in a local group of a machine using GPO |
| Get-DomainGPOUserLocalGroupMapping -Identity \<username\> -Verbose | Get machines where the username is a member of a specific group |
| Find-LocalAdminAccess -Verbose | Find all machines on the current domain with the current user has local admin access |
| Find-DomainUserLocation -Verbose | Find computers where a domain admin has a session |
| Find-DomainUserLocation -UserGroupIdentity "RDPUsers" | Find computers where a domain admin has a session, by group |
| Get-DomainGroupMember | Gets a list of group members for a given group, Domain Admins by default |
| Find-DomainUserLocation -CheckAccess | Similar to Find-LocalAdminAccess this finds computers where a domain admin session is available |
| 

---

| PowerShell AD Module | Description |
| ---------------------------- | ---------------------------- |
| Get-ADDomain | Gets domain information |
| Get-ADDomain -Identity domain.local | Gets specific domain information | 
| (Get-ADDomain).DomainSid | Gets the SID for the current domain |
| Get-ADDefaultDomainPasswordPolicy | Gets AD Domain Policy |
| Get-ADDefaultDomainPasswordPolicy -Identity domain.local | Gets AD Doamin Password Policy | 
| Get-ADDomainController | Gets information about the domain controller(s) |
| Get-ADDomainController -DomainName domain.local -Discover | Gets domain controller(s) for another domain |
| Get-ADUser -Filter * -Properties * | Gets information about all AD users |
| Get-ADUser -Identity username -Properties * | Gets information about a single AD user |
| Get-ADUser -Filter * -Properties * | Gets all properties for all users in the domain |
| Get-ADUser -Filter 'Description -like "\*built\*"' -Properties Description \| select name,Description | Search domain users with specific attributes |
| Get-ADUser -Filter * -Properties * \| select samaccountname, description, whenchanged | AD Module example to filter domain users by properties |
| Get-ADUser -Filter * -Properties * \| select SamAccountName,PasswordLastSet | Another example of filtering properties |
| Get-ADUser -Filter * -Properties * \| select name,description | Check description field for passwords |
| Get-ADUser -Properties * -LDAPFilter '(&(objectCategory=user)(description=*))' \| select samaccountname,description | Check description field for passwords (alternate)
| Get-ADUser -Filter "name -eq 'sally jones'" | Get single AD user syntax 1 |
| Get-ADUser -Filter {name -eq 'sally jones'} | Get single AD user syntax 2 |
| Get-ADUser -Filter 'name -eq "sally jones"'| Get single AD user syntax 3 |
| Get-ADUser -filter {-name -like "joe\*"} | Get AD user where name like |
| Get-ADUser -Properties * -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=524288)' \| select Name,memberof, servicePrincipalName,TrustedForDelegation \| fl | Get-ADUser (TrustedForDelegation) |
| Get-ADUser -filter {adminCount -eq '1' -and DoesNotRequirePreAuth -eq 'True'} | Get-ADUser (DoesNotRequirePreAuth) ASRepRoasting on Admin accounts |
| Get-ADUser -Filter "adminCount -eq '1'" -Properties \* \| where servicePrincipalName -ne $null \| select SamAccountName,MemberOf,ServicePrincipalName \| fl | Get-ADUser (with servicePrincipalName) can likely be Kerberoasted | 
| (Get-ADUser -Filter * -SearchBase "OU=Former Employees,DC=INLANEFREIGHTENUM1,DC=LOCAL").count | Get-ADUser (count members in a group) |
| Get-AdUser -LDAPFilter '(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))(adminCount=1)' -Properties * \| select name,memberof \| fl | Get admins with blank passwords |
Get-AdUser -LDAPFilter '(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))(adminCount=1)' -Properties * \| select name,memberof \| fl | Get users with blank passwords |
| Get-ADComputer -Filter * \| select Name | Gets a list of computers in the domain |
| Get-ADComputer -Filter 'OperatingSystem -like "\*Server 2016\*"' -Properties OperatingSystem \| select Name,OperatingSystem | Gets a list of computers in the domain running Server 2016 |
| Get-ADComputer -Filter "DNSHostName -like 'SQL\*'" | Find ADComputer where name is like SQL |
| Get-ADComputer -Properties * -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=524288)' \| select DistinguishedName,servicePrincipalName,TrustedForDelegation \| fl | Get-ADComputer (TrustedForDelegation) |
| Get-ADGroup -Filter \* \| select Name | Get all the groups in the current domain |
| Get-ADGroup -Filter \* -Properties \* | Get all group propertues in the current domain |
| Get-ADGroup -Filter "adminCount -eq 1" \| select Name | Find AD groups and filter for Admins | 
| Get-ADGroupMember -Identity 'Service Technicians' \| ?{$\_.ObjectClass -eq "Group"} \| %{Write-Host $_.Name;Get-ADGroupMember $_ } | Get-ADGroupMember (find all members of group) |
| Get-ADGroup -filter * -Properties MemberOf \| Where-Object {$_.MemberOf -ne $null} \| Select-Object Name,MemberOf | Get-ADGroupMember (find all nest groups) |
| Get-ADGroup -Filter 'member -RecursiveMatch "CN=Harry Jones,OU=Network Ops,OU=IT,OU=Employees,DC=INLANEFREIGHT,DC=LOCAL"' \| select name | Recursive search for all groups of a member |
| Get-ADGroup -Filter 'Name -like "\*admin\*" | Get all groups containing the word "admin" |
| Get-ADGroupMember -Identity "Domain Admins" -Recursive | Get all members of the Domain Admins Group | 
| Get-ADPrincipalGroupMembership -Identity username | Get the group membership for \<username\> |







## Appendix 
- [PowerView -ReadTheDocs](https://powersploit.readthedocs.io/en/stable/Recon/README/#powerview)
- [Powershell Active Directory Module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps)
- [HackTricks PowerView](https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters/powerview)