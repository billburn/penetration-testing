
| Command | Description |
| ---------------------------- | ---------------------------- |
| net accounts | Returns information about password requirements |
| net accounts | /domain | Returns domain password and lockout policy |
| net group /domain	| Returns domain group information |
| net group "Domain Admins" /domain	| Returns users with the Domain Admin privilege |
| net group "domain computers" /domain | List of PCs connected to the domain |
| net group "Domain Controllers" /domain | 	List of PC accounts of domain controllers |
| net group (domain_group_name) /domain | Returns a list of user(s) in the group, for the domain |
| net groupss /domain | List of domain groups |
| net localgroup | Returns all available groups |
| net localgroup Administrators | Returns members of the local administrators group |
| net localgroup administrators \[username\] /add	| Adds the \[username\] to the local administrator group |
| net share	| Returns a list of shares on the host |
| net user \<account_name\> /domain | Returns information about a user within the domain |
| net user /domain | Returns all users in the domain |
| net user %username% | Returns information about the current user |
| net use x: \computer\share | Mount the share 'share' locally |
| net view | Get a list of computers |
| net view /all /domain:\[domain_name\] | Get a list of shares on the domain |
| net view \computer /ALL | Lists shares on a specific computer |
| net view /domain | Returns a list of PCs of the domain |