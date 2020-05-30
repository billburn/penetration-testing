# Windows Enumeration Tips
 
 ## Searching files with dir
 ```
 [@swisskyrepo] https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md
 
 dir /S /B filename*.txt
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