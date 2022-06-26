#!/bin/bash

for password in $(cat passwords.txt); do
	openssl passwd -5 pass:$password >> sha256-hashes.txt
done
