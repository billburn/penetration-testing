# Powershell and PowerView Commands Side-by-Side Comparison

## Active Directory Domain Enumeration
| PowerView Command | ActiveDirectory Module | Description |
| ---------------------------- | ---------------------------- | ---------------------------- |
| Get-NetDomain | Get-ADDomain | Gets domain information |
| Get-NetDomain -Domain domain.local | Get-ADDomain -Identity domain.local | Gets specific domain information | 
| Get-DomainSid | (Get-ADDomain).DomainSid | Gets the SID for the current domain |
| Get-DomainPolicyData | Get-ADDefaultDomainPasswordPolicy | Gets AD Doamin Policy |
| Get-DomainPolicyData -domain domain.local | Get-ADDefaultDomainPasswordPolicy -Identity domain.local | Gets AD Doamin Password Policy | 
| (Get-DomainPolicyData).systemaccess | NA | PowerView prettified version of the domain policy |
| (Get-DomainPolicyData).kerberospolicy | NA | PowerView prettified version of the kerberos policy |
| Get-DomainController | Get-ADDomainController | Gets information about the domain controller(s) |
| Get-DomainController -Domain domain.local | Get-ADDomainController -DomainName domain.local -Discover| Gets domain controller(s) for another domain |
| Get-DomainUser * | Get-ADUser -Filter * -Properties * | Gets information about all AD users | 
| Get-DomainUser -Identity username | Get-ADUser -Identity username -Properties * | Gets information about a single AD user |
| Get-DomainUser -Identity username -Properties * | Get-ADUser -Filter * -Properties * | Gets all properties for all users in the domain |
| Get-DomainUser -LdapFilter "Description=\*Built\*" \| Select name, description | Get-ADUser -Filter 'Description -like "\*built\*"' -Properties Description \| select name,Description | Search domain users with specific attributes |
| Get-NetUser \| select samaccountname, description, pwdlastset | | PowerView example to filter domain users by properties |
| NA | Get-ADUser -Filter * -Properties * \| select samaccountname, description, whenchanged | AD Module example to filter domain users by properties |
| Get-NetUser -properties name, pwdlastset, etc... | Get-ADUser -Filter * -Properties * \| select SamAccountName,PasswordLastSet | Another example of filtering properties |
| Get-NetUser -properties name, description | Get-ADUser -Filter * -Properties * \| select name,description | Check description field for passwords |
| Get-DomainComputer \| select Name | Get-ADComputer -Filter * \| select Name | Gets a list of computers in the domain |
| Get-DomainComputer -OperatingSystem "\*Server 2016\*" | Get-ADComputer -Filter 'OperatingSystem -like "\*Server 2016\*"' -Properties OperatingSystem \| select Name,OperatingSystem | Gets a list of computers in the domain running Server 2016 |
| Get-DomainGroup \| select Name | Get-ADGroup -Filter \* \| select Name | Get all the groups in the current domain |
| Get-DomainGroup -Domain domain.local \| select Name | Get-ADGroup -Filter \* -Properties \* | Get all group propertues in the current domain |


## Appendix 
- [PowerView -ReadTheDocs](https://powersploit.readthedocs.io/en/stable/Recon/README/#powerview)
- [Powershell Active Directory Module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps)
- [HackTricks PowerView](https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters/powerview)