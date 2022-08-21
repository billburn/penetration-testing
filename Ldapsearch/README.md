# Ldapsearch

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