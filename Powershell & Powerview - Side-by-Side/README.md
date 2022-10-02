# Powershell and PowerView Commands Side-by-Side Comparison

## Active Directory Domain Enumeration
| PowerView Command | ActiveDirectory Module | Description |
| ---------------------------- | ---------------------------- | ---------------------------- |
| Get-NetDomain | Get-ADDomain | Gets domain information |
| Get-NetDomain -Domain domain.local | Get-ADDomain -Identity domain.local | Gets specific domain information | 
| Get-DomainSid | (Get-ADDomain).DomainSid | Gets the SID for the current domain |