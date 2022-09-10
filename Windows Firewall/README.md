# Windows Firewall

## Is Firewall Enabled
```
Get-NetFirewallProfile | Format-Table Name, Enabled
```

## Get Firewall Rules
```
Get-NetFirewallRule | select DisplayName, Enabled, Description
```

## Disable Firewall (requires admin)
```
Set-NetFirewallProfile -Profile Domain, Public, Private -Enabled False
Get-NetFirewallProfile | Format-Table Name, Enabled
```

## Test Firewall Connectivity through Firewall
```
Test-NetConnection -ComputerName 127.0.0.1 -Port 80
(New-Object System.Net.Sockets.TcpClient("127.0.0.1", "80")).Connected
```