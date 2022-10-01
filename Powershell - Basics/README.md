# PowerShell Basics

## PowerShell Basic Commands

| Command | Summary |
| ---------------------------- | ---------------------------- |
| Get-Help Get-FileHash | This command gets the help page for the cmdlet you are trying to run |
| Get-Help process | This finds all cmdlets with process in the name |
| Get-Help Get-FileHash -Full | This requests the full help documentation |
| Get-Help Get-FileHash -Examples | This requests examples for the cmdlet you requested |
| Get-Command -CommandType cmdlet | This provides a list of ALL available cmdlets on your system |
| Get-Process | This lists the processes running on your host (like ps -aux on nix) |
| Get-Command -Module Get-FileHash | Provides a list of all commands in module | 

## Importing Module
```
Import-Module <name of ps1>
OR
. .\powershell-script.ps1
```

## Checking Services
```
get-service AdvancedSystemCareService9
stop-service AdvancedSystemCareService9
start-service AdvancedSystemCareService9

powershell -c get-service AdvancedSystemCareService9
powershell -c stop-service AdvancedSystemCareService9
powershell -c start-service AdvancedSystemCareService9
```