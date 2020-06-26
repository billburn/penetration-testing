# Kerberos

## Tickets
```
Kerbrute Enumeration - No domain access required 
Pass the Ticket - Access as a user to the domain required
Kerberoasting - Access as any user required
AS-REP Roasting - Access as any user required
Golden Ticket - Full domain compromise (domain admin) required 
Silver Ticket - Service hash required 
Skeleton Key - Full domain compromise (domain admin) required
```

## Kerbrute
```
* Be sure to update the /etc/hosts file to point to the correct DC
$./kerbrute_linux_amd64 userenum --dc CONTROLLER.local -d CONTROLLER.local ad-users.txt -v
```