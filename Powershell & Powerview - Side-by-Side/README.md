# Powershell and PowerView Commands Side-by-Side Comparison

## Active Directory Domain Enumeration
| PowerView Command | ActiveDirectory Module | Description |
| ---------------------------- | ---------------------------- | ---------------------------- |
| Get-NetDomain | Get-ADDomain | Gets domain information |
| Get-NetDomain -Domain domain.local | Get-ADDomain -Identity domain.local | Gets specific domain information | 
| Get-DomainSid | (Get-ADDomain).DomainSid | Gets the SID for the current domain |
| Get-DomainPolicy -Domain domain.local | Get-ADDefaultDomainPasswordPolicy -Identity domain.local | Gets AD Doamin Password Policy | 
| (Get-DomainPolicy)."systemaccess" | NA | PowerView prettified version of the domain policy |
| (Get-DomainPolicy)."kerberospolicy" | NA | PowerView prettified version of the kerberos policy |
| Get-NetDomainController | GetADDomainController | Gets information about the domain controller(s) |
| Get-NetDomainController -Domain domain.local | GetADDomainController -DomainName domain.local | Gets domain controller(s) for another domain |
| Get-Netuser * | Get-ADUser -Filter * -Properties * | Gets information about all AD users | 
| Get-NetUser -Username username | Get-ADUser -Identity username -Properties * | Gets information about a single AD user |
| Get-UserProperty | Get-ADUser -Filter -Properties * | Gets all properties for all users in the domain |
| Get-NetUser \| select samaccountname, description, pwdlastset | | PowerView example to filter domain users by properties |
| NA | Get-ADUser -Filter * -Properties * \| select samaccountname, description, whenchanged | AD Module example to filter domain users by properties |
| Get-NetUser -properties name, pwdlastset, etc... | Get-ADUser -Filter * -Properties * \| select SamAccountName,PasswordLastSet | Another example of filtering properties |
| Get-NetUser -properties name, description | Get-ADUser -Filter * -Properties * \| select name,description | Check description field for passwords |


## Appendix 
[PowerView -ReadTheDocs](https://powersploit.readthedocs.io/en/stable/Recon/README/#powerview)
[Powershell Active Directory Module](https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps)
[HackTricks PowerView](https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters/powerview)