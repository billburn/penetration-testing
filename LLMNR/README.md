# Responder and Inveigh

## Responder Data
- Data is stored in /usr/share/responder/logs
- Defautl database is /usr/share/responder/Responder.db (sqlite DB)
- Default configuration file is /usr/share/responder/Responder.conf
- If relaying with nltmx make sure to disable smb in Responder.conf ^^

## Responder Usage
```
## Analyze Mode
responder -I eth0 -A 

## Active Intercept
responder -I eth0 -Pwd
```

## Legacy versions of Responder
```
responder -I eth0 -wrf
```