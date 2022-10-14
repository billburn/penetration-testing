# PowerShell Active Directory Enumeration

## Get Current AD Domain
```
$ADClass = [System.DirectoryServices.ActiveDirectory.Domain]
$ADClass::GetCurrentDomain()
```

## Get-ADUser
All three are valid syntaxes

```
`Get-ADUser -Filter "name -eq 'sally jones'"`
`Get-ADUser -Filter {name -eq 'sally jones'}`
`Get-ADUser -Filter 'name -eq "sally jones"'`
```

## Get-ADUser (wildcard for any user name with joe)
```
Get-ADUser -filter {-name -like "joe*"}
```

## Get-ADComputer (filter for hostnames with SQL)
```
Get-ADComputer -Filter "DNSHostName -like 'SQL*'"
```

## Get-ADGroup (filter for admin users)
```
Get-ADGroup -Filter "adminCount -eq 1" | select Name
```

## Get-ADUser (DoesNotRequirePreAuth) ASRepRoasting on Admin accounts
```
Get-ADUser -filter {adminCount -eq '1' -and DoesNotRequirePreAuth -eq 'True'}
```

## Get-ADUser (with servicePrincipalName) can likely be Kerberoasted
```
Get-ADUser -Filter "adminCount -eq '1'" -Properties * | where servicePrincipalName -ne $null | select SamAccountName,MemberOf,ServicePrincipalName | fl
```

## Get-ADUser (search descrption field) - can contain passwords
```
Get-ADUser -Properties * -LDAPFilter '(&(objectCategory=user)(description=*))' | select samaccountname,description
```

## Get-ADUser (TrustedForDelegation)
```
Get-ADUser -Properties * -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=524288)' | select Name,memberof, servicePrincipalName,TrustedForDelegation | fl
```

## Get-ADComputer (TrustedForDelegation)
```
Get-ADComputer -Properties * -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=524288)' | select DistinguishedName,servicePrincipalName,TrustedForDelegation | fl
```

## Get-ADUser (Users, in this case Admins, allowing blank password)
```
Get-AdUser -LDAPFilter '(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))(adminCount=1)' -Properties * | select name,memberof | fl
```

## Get-ADGroupMember (of "Security Operations" group)
```
Get-ADGroupMember -Identity "Security Operations"
```

## Get-ADGroupMember (recursive search for all groups, of a member)
```
Get-ADGroup -Filter 'member -RecursiveMatch "CN=Harry Jones,OU=Network Ops,OU=IT,OU=Employees,DC=INLANEFREIGHT,DC=LOCAL"' | select name
```

## Get-ADUser (count of all users in Employees/IT OU structure)
```
(Get-ADUser -SearchBase "OU=IT,OU=Employees,DC=INLANEFREIGHT,DC=LOCAL" -SearchScope Subtree -Filter *).count
```

## Get-ADGroup (find all nested groups)
```
Get-ADGroup -filter * -Properties MemberOf | Where-Object {$_.MemberOf -ne $null} | Select-Object Name,MemberOf
```

## Get-ADGroupMember (find all members of group)
Get-ADGroupMember -Identity 'Service Technicians' | ?{$_.ObjectClass -eq "Group"} | %{Write-Host $_.Name;Get-ADGroupMember $_ }

## Get-ADUser (count members in a group)
```
(Get-ADUser -Filter * -SearchBase "OU=Former Employees,DC=INLANEFREIGHTENUM1,DC=LOCAL").count
```

## Get-ADGroup (where adminCount = 1)
```
Get-ADGroup -Filter "adminCount -eq 1"
```

## Check Languge Contrained Mode
There are three modes:
- NoLanguage
- FullLanguage
- ConstrainedLanguage

```
$ExecutionContext.SessionState.LanguageMode
```

