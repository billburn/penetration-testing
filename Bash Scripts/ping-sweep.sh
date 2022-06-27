#!/bin/bash

for i in `seq 1 254`; do
    ping -c 1 '192.168.10.'$i |grep "64 bytes" | cut -d " " -f4 | tr -d ":" &
done