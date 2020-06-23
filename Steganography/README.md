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

## Steghide Extract Data from File
```
* In this example there is no password; you may need to brute-force password with stegcracker first
steghide extract -sf Extinction.jpg -xf data
```

## QR Code Reader
```
[URL] https://zxing.org/w/decode.jspx
Upload the file or provide a URL to decode
```