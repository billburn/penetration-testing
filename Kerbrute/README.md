# Kerbrute

## Kerbrute Usage
Be sure to update the /etc/hosts file to point to the correct DC

```
./kerbrute_linux_amd64 userenum --dc CONTROLLER.local -d CONTROLLER.local ad-users.txt -v
./kerbrute_linux_amd64 userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users.txt
```
