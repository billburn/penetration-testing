# Local Administrator Password Solutions (LAPS)

## Find Groups that have LAPS installed
```
Find-LAPSDelegatedGroups
```

## Find Hosts and Identities with LAPS installed
```
Find-AdmExtendedRights
```

## Get-LAPS Computers (if permissions allowed, you will get plaintext passwords)
```
Get-LAPSComputers
```