# Hashcat Common Commands

## NTLM
```
 hashcat64.exe -m 1000 <hash.name> rockyou.txt
```

## SHA-256
```
hashcat -m 1400 <hash.name> rockyou.txt
```