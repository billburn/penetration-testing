# Hashcat Common Commands

## Rules
-r best64.rule
-O optmized
-w3 workers

## NTLM
```
 hashcat64.exe -m 1000 <hash.name> rockyou.txt
```

## SHA-256
```
hashcat -m 1400 <hash.name> rockyou.txt
```

## SHA-512
```
hashcat64.exe -m 1800 ..\hashes\game_zone-root.hash ..\wordlists\rockyou.txt -O -w3 -r .\rules\best64.rule
```