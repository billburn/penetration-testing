# Password Hunting

| Command	| Summary |
| --------- | ---------------------------- |
| findstr /si password *.txt | Searches the computer for the string password in all text files |
| findstr /si password *.xml | Searches the computer for the string password in all xml files |
| findstr /si password *.ini | Searches the computer for the string password in all ini files |
| netsh wlan show profile | Returns the wifi AP SSID |
| netsh wlan show profile <SSID> key=clear | Returns the wifi password, in cleartext |