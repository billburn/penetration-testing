# PowerShell Credntials

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