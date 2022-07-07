# Ldapsearch

## Initial Ldap Enumeration
```
ldapsearch -H ldap://10.10.10.182 -x -s base namingcontexts
ldapsearch -x -H ldap://active.htb -s base namingcontexts
```