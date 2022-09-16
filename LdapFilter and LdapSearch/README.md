# LdapFilter and LdapSearch

## Ldapsearch to get Naming Contexts
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

## LdapWiki
To run any of these queries be sure to use the Get-AdObject cmdlet with the -LdapFilter ' Enter Command Here'

```
Get-AdObject -LdapFilter '(ObjectClass=group)'
```

- [User Queries](https://ldapwiki.com/wiki/Active%20Directory%20User%20Related%20Searches)
- [Group Queries](https://ldapwiki.com/wiki/Active%20Directory%20Group%20Related%20Searches)
- [Computer Queries](https://ldapwiki.com/wiki/Active%20Directory%20Computer%20Related%20LDAP%20Query)