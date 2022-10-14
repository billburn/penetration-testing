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

## Get PowerShell Version
```
(Get-ItemProperty HKLM:\Software\Microsoft\PowerShell\*\PowerShellEngine -Name PowerShellVersion).PowerShellVersion
```

## Get Currently Loaded Variables
```
Get-ChildItem Variable:\
```

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

## Running Executable
```
c:\> start-process shell.exe
c:\> .\shell.exe
```

## Searching for files names with PowerShell
```
Get-Childitem –Path C:\ -Include *search-string* -File -Recurse
```

 ## Decoding Base64
 ```
 $string = "some-base64 aksdjklasd=="
 [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($string))
  ```

## Reading Users PowerShell History
```
%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

## Search all files for keyword
```
type * | findstr "password"
```

## Checking PowerShell History
Powershell.exe does not recognize or use the %% reference, so need to use env variables

```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt (cmd.exe)
type $Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt (powershell.exe)
```

## Get List of Installed Software
```
get-ciminstance win32_product | fl
```

## Get a list of Installed Software (exclude Microsoft)
```
get-ciminstance win32_product -Filter "NOT Vendor like '%Microsoft%'" | fl
```

## Ways to Bypass Execution Policy
```
powershell -ExecutionPolicy bypass -NoProfile
powershell -c <cmd>
powershell -encodedcommand
$env:PSExecutionPolicyPreference="bypass"
```



## Escape Characters
| Character | Escaped As | Note |
| ---------------------------- | ---------------------------- | ---------------------------- |
| " | \\" | Only needed if the data is enclosed in double-quotes |
| ' | \\' | Only needed if the data is enclosed in single-quotes |
| NUL | \00 | Standard LDAP escape sequence |
| \ | \5c | Standard LDAP escape sequence |
| * | \2a | Escaped automatically, but only in -eq and -ne. Use -like and -notlike for wildcard comparison |
| () | 28 | Escaped automatically |
| ) | 29 | Escaped automatically |
| / | /2f | Escaped automatically |


## PowerShell Operators
| Filter | Meaning |
| ---------------------------- | ---------------------------- |
| -eq	| Equal to |
| -le	| Less than or equal to |
| -ge	| Greater than or equal to |
| -ne	| Not equal to |
| -lt	| Less than |
| -gt	| Greater than |
| -approx | Approximately equal to |
| -bor | Bitwise OR |
| -band	| Bitwise AND |
| -recursivematch	| Recursive match |
| -like | Like |
| -notlike| Not Like |
| -and| Boolean AND |
| -or	| Boolean OR |
| -not |Boolean NOT |
