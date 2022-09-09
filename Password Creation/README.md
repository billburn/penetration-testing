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