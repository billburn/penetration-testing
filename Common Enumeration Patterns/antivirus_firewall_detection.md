# Antivirus and Firewall Detection

| Command	| Summary |
| --------- | ---------------------------- |
| sc query windefend | Returns information about the Windows Defender service, and its it currently running |
| sc queryex type= service | Returns information about all running services | 
| netsh advfirewall firewall dump | Returns details about all of the firewall rules |
| netsh firewall show state | Returns information about the firewall state |
