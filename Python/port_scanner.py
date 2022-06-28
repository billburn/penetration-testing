#!/usr/bin/env python3
#Author: Bill Burn

import click
import sys
import socket
from datetime import datetime

click.clear()

## Define Target
if len (sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")

## Banner
print("-" * 50)
print("Scanning target " + target)
print("Time started:" + str(datetime.now()))
print("-" * 50)

try:
    for port in range(22,23):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # returns error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting program")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error():
    print("Couldnt connect to server")
    sys.exit()