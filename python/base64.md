# Base64

## TryHackMe Challenge to decode a textfile
```
#!/usr/bin/env python3
import base64

fo = open("encodedflag.txt","r")
data = fo.read()

b16_data1 = base64.b16decode(data)
b16_data2 = base64.b16decode(b16_data1)
b16_data3 = base64.b16decode(b16_data2)
b16_data4 = base64.b16decode(b16_data3)
b16_data5 = base64.b16decode(b16_data4)
#print(b16_data5)

b32_data1 = base64.b32decode(b16_data5)
b32_data2 = base64.b32decode(b32_data1)
b32_data3 = base64.b32decode(b32_data2)
b32_data4 = base64.b32decode(b32_data3)
b32_data5 = base64.b32decode(b32_data4)
#print(b32_data5)

b64_data1 = base64.b64decode(b32_data5)
b64_data2 = base64.b64decode(b64_data1)
b64_data3 = base64.b64decode(b64_data2)
b64_data4 = base64.b64decode(b64_data3)
b64_data5 = base64.b64decode(b64_data4)
print(b64_data5)

fo.close()
```