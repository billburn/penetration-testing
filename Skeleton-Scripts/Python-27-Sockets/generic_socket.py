#!/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	#print "\nSENDING EVIL BUFFER"
	address = raw_input("Enter address to fuzz: ")
	port = int(raw_input("Enter port to fuzz: "))
	s.connect((address, port))
	data = s.recv(1024)
	print data

	username = raw_input("Enter user to fuzz: ")
	s.send('USER %s' + username + '\r\n')
	data = s.recv(1024)
	print data

	password = raw_input("Enter password to fuzz: ")
	s.send('PASS %s' + password + '\r\n')
	data = s.recv(1024)
	print data

	s.close()

except:
	print "Could not connect to POP3 Server"