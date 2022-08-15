# NTDS Command Line Recovery

## Sync NTDS to Location (have to be elevated)
```
powershell ntdsutil.exe 'ac i ntds' 'ifm' 'create full c:\users\public\' q q
```