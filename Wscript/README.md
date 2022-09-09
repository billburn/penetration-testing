# WScript and CScript Commands

## Simple calc.exe example
```
Set WshShell = WScript.CreateObject("WScript.Shell")
WshShell.Run("C:\Windows\System32\calc.exe " & WScript.ScriptFullName),0,True
```

## If VBS Files are Deny Listed
- Create your VBS file, and run with /e switch
```
wscript /e:vbscript c:\users\thm\desktop\payload.txt
```