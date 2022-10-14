# PowerShell Remoting

## Enable PS Remoting on Server
```
Enable-PSRemoting
```

## Enable WinRM on Client
```
start-service winrm
ls wsman:\localhost\Client\TrustedHosts
```

## Set Trusted Host on Client
```
set-item wsman:\localhost\Client\TrustedHosts -value 192.168.10.15
```

## Create New-PSSession
This options will prompt you with the GUI credential box
```
New-PSSession -ComputerName 192.168.10.15 -Credential (Get-Credential) 
```

## Enter-PSSession
```
Enter-PSSession <num>
```

## Create New-PSSession with Credentials
```
$username = 'Administrator'
$password = 'P@ssw0rd123'
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ($username, $securePassword)
New-PSSession -ComputerName 192.168.10.15 -Credential $cred
Get-PSsession
Enter-PSSession <num>
```

## Get all PSSessions
```
Get-PSSession
```

## Delete all PSSessions
```
Get-PSSession | Remove-PSSession
```

[Microsoft Help for PSSession](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/remove-pssession?view=powershell-7.2)