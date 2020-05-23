# Base64

## TryHackMe Challenge to decode a textfile using a loop
```
#!/usr/bin/env python3
import base64

fo = open("b64.txt", "r")
data = fo.read()

i = 1
while i <51:
        b64_data = base64.b64decode(data)
        data = b64_data
        print(i)
        print(b64_data)
        i += 1

fo.close()
```