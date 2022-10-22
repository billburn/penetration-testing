# PowerShell Remoting

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

| PowerShell Remoting | Description |
| ---------------------------- | ---------------------------- |
| Enable-PSRemoting | Enables PowerShell Remoting |
| Get-PSSession | Lists all PS Sessions |
| Get-PSSession \| Remove-PSSession | Removes the current PS Session |
| Invoke-Command -ScriptBlock {Get-Process} -ComputerName \<computer_name\> | Requires privileges, but will remotely list process on remote host |
| $sess = New-PSSession -ComputerName dcorp-adminsrv | Save a PS Remote session into a variable |
| Invoke-Command -Session $sess -ScriptBlock {$proc = Get-Process} | Save Processes from remote ession in a variable | 
| Invoke-Command -Session $sess -ScriptBlock {$proc} | Using stateful command, running the same get-process command on the remote host |

[Microsoft Help for PSSession](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/remove-pssession?view=powershell-7.2)