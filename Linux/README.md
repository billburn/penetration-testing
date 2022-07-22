# Linux Enumeration Tips

## Default Ubuntu File Permissions
```
* Folders should be 0755
* Files shuld be 0664
find /home/user -type d -print0 | xargs -0 chmod 0775
find /home/user -type f -print0 | xargs -0 chmod 0664
```

## Grep all file for string
```
grep -ilR "flag11" / 2>/dev/null
```

## Remove all newline space from file 
```
tr -d "\n\r" < yourfile.txt
```

## Remove specific character or space from Nano
```
ctrl + \
search the file _char
replace the file _char
choose option
```

## Find SUID Files
```
find / -perm -u=s -type f 2>/dev/null
```

## cat not working
```
Have you tried less?
```

## Convert all UPPER to lower or lower to UPPER
```
cat TEXT or filename.txt | tr [:upper:] [:lower:]
```

## Send Email Message with Attachment
```
sendemail -t nico@megabank.com -f badguy@ph0enix.local -s reel.htb.local -u RTF -m "Important" -a invoice.rtf
```

 ## Mount a VHD Drive
 - ```--add`` is the name of the file
 ```
 mkdir /mnt/vhd
 sudo guestmount --add 9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd --inspector --ro -v /mnt/vhd
 ```