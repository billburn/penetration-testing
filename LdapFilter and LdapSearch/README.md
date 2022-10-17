# LdapFilter and LdapSearch

## SearchBase
SearchBase is a parameter that specifies an ActiveDirectory path to search in a specific OU
```
"OU=Employees,DC=DomainName,DC=LOCAL"
```

## SearchScope
SearchScope allow us to define how deep into the OU hierarchy we would like to search.  SearchScope has three levels

| Name | Level | Description |
| ---------------------------- | ---------------------------- | ---------------------------- |
| Base | 0 | The object us specified as the SearchBase |
| OneLevel | 1 | Searches for objects in the container defined by SearchBase, but not in any sub-containers |
| SubTree | 2 | Searches for objects contained by the SearchBase and all child containers, recursively |

## Ldapsearch to get Naming Contexts (anonymous)
```
ldapsearch -H ldap://10.10.10.182 -x -s base namingcontexts
ldapsearch -x -H ldap://forest.htb.local -s base namingcontexts
```

## Ldapsearch with basedn
```
ldapsearch -x -H ldap://forest.htb.local -b "dc=htb,dc=local"
```

## Ldapsearch with objectclass = person
```
ldapsearch -x -H ldap://forest.htb.local -b "dc=htb,dc=local" -W "(objectclass=person)"
```

## Ldapsearch with objectclass = person and filter of SamAccountName
```
ldapsearch -x -H ldap://forest.htb.local -b "dc=htb,dc=local" -W "(objectclass=person)" sAMAccountName
```

## LDAP Query - User Related Search (on the host)
```
Get-ADObject -LdapFilter '(objectClass=Group)' | select cn
```

## LDAP Query - Administratively disabled accounts (on the host)
```
Get-ADObject -LDAPFilter '(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))' | select samaccountname,useraccountcontrol
```

## Windapsearch (get Domain functional level)
```
python windapsearch.py --dc-ip 10.129.42.188 -u "" --functionality
```

## Windapsearch (get all domain users)
```
python3 windapsearch.py --dc-ip 10.129.1.207 -u "" -U
```

## Windapsearch (Domain Admins)
```
python windapsearch.py -d INLANEFREIGHT.LOCAL --dc-ip 172.16.5.5 -u forend@inlanefreight.local -p Klmcargo2 --da
```

## Windapsearch (Priviged Users)
```
python windapsearch.py -d INLANEFREIGHT.LOCAL --dc-ip 172.16.5.5 -u forend@inlanefreight.local -p Klmcargo2 -PU
```

## Ldapsearch-ad (get password policy)
```
python ldapsearch-ad.py -l 10.129.113.91 -d domain.local -u james.cross -p 'enter_password' -t pass-pols
```

## Ldapsearch-ad (get kerberoastable users)
```
python ldapsearch-ad.py -l 10.129.113.91 -d inlanefreight -u james.cross -p 'Academy_Student!' -t kerberoast 
```

## Ldapsearch-ad (get asrep-roastable users)
```
python ldapsearch-ad.py -l 10.129.113.91 -d inlanefreight -u james.cross -p 'Academy_Student!' -t asreproast
```

## Ldapearch (get password policy)
```
ldapsearch -h 172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "*" | grep -m 1 -B 10 pwdHistoryLength
```

## Ldapsearch (get users)
```
ldapsearch -h 172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"  | grep sAMAccountName: | cut -f2 -d" "
```

## LdapWiki
To run any of these queries be sure to use the Get-AdObject cmdlet with the -LdapFilter ' Enter Command Here'

```
Get-AdObject -LdapFilter '(ObjectClass=group)'
```

- [User Queries](https://ldapwiki.com/wiki/Active%20Directory%20User%20Related%20Searches)
- [Group Queries](https://ldapwiki.com/wiki/Active%20Directory%20Group%20Related%20Searches)
- [Computer Queries](https://ldapwiki.com/wiki/Active%20Directory%20Computer%20Related%20LDAP%20Query)