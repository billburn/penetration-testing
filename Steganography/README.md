# Stego CTF Challenges

## Binwalk Extract Files
```
$binwalk -e <name of file>
```

## Stegcracker
```
* Install: pip3 install stegcracker (steghide is a prerequisite)
$stegcracker <name of file> <wordlist>
$stegcracker aa.jpg /usr/share/wordlist/rockyou.txt
```