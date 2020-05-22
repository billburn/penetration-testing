## Python2 Sockets


```
#!/usr/bin/python
#author: bill burn
## Redevelop in python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(raw_input("Enter a port: "))

s.connect((sys.argv[1], port))

while 1:
    userInput = raw_input("Enter a String: ")
    s.send(userInput)
    print s.recv(2048)

s.close()
```