# Powershell and PowerView Commands Side-by-Side Comparison

## Active Directory Domain Enumeration
| PowerView Command | ActiveDirectory Module | Description |
| ---------------------------- | ---------------------------- | ---------------------------- |
| Get-NetDomain | Get-ADDomain | Gets domain information |
| Get-NetDomain -Domain domain.local | Get-ADDomain -Identity domain.local | Gets specific domain information | 
| Get-DomainSid | (Get-ADDomain).DomainSid | Gets the SID for the current domain |
| Get-DomainPolicy -Domain domain.local | Get-ADDefaultDomainPasswordPolicy -Identity domain.local | Gets AD Doamin Password Policy | 
| (Get-DomainPolicy)."systemaccess" | NA | PowerView prettified version of the domain policy |
| (Get-DomainPolicy)."kerberospolicy" | NA | PowerView prettified version of the kerberos policy|
