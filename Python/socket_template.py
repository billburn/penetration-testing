#!/usr/bin/env python3
#Author: Bill Burn

import click
import socket
click.clear()

host = "192.168.10.13"
port = 8000 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))