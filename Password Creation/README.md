# Password Creating Tools
TryHackMe has a great room on this called: "passwordattacks"

[Tryhackme 'PasswordAttacks'](https://tryhackme.com/room/passwordattacks)

## Gorilla

[Gorilla GitHub](https://github.com/d4rckh/gorilla)

## Crunch
This tool allows us to create passwords for a given keyspace

[Crunch](https://github.com/jim3ma/crunch)

## CUPP - Common User Passwords Profiler
This tool allows us to generate a password list based on information about the target

[CUPP](https://github.com/Mebus/cupp)

## John
```
john --wordlist=/tmp/single-password-list.txt --rules=best64 --stdout > output.txt
john --wordlist=/tmp/single-password-list.txt --rules=KoreLogic --stdout > output.txt
```

## Creating Custom Wordlist for Password Spray

1. Start by creating a sample list of words
2. Run small Bash for loop to add years
3. Try quick wins with username / username as the password

```
## Custom Words
January
February
March
April
May
June
July
August
September
October
November
December
Password
P@ssw0rd
htb
Secret
Autumn
Fall
Spring
Summer

## Custom Years and Exclamation
for i in  $(cat custom-wordlist.txt); do echo $i; echo ${i}\!; echo ${i}2018; echo ${i}2018\!; echo ${i}2019; echo ${i}2019\!; echo ${i}2020; echo ${i}2020\!; echo ${i}2021; echo ${i}2021\!; echo ${i}2022; echo ${i}2022\!; done > password.txt

## Modify with Hashcat Password Rules
hashcat --force --stdout passwords.txt -r /usr/share/hashcat/rules/best64.rule -r /usr/share/hashcat/rules/toggles1.rule |sort -u | awk 'length ($0) > 8' > password_spray_final.txt
```