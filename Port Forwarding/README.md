# Port Forwarding

## Local Port Forward
```
$ssh -L <bind port local>:remote-system:<host-port> bob@192.168.10.10 -N &
$ssh -L 10000:localhost:10000 ph0enix@10.2.3.85

[NOTE] -N is do not execute a remote command (also known as do not start shell).  This is useful for just forwarding ports.
[NOTE] & is to background the command
```

## Dynamic Port Forward
```
[NOTE] In this example we have access to a machine that fronts a number of other machines in the 192.168.10.0/x network
$ssh -D 1080 bob@192.168.10.10 
```

## Remote Port Forward
```
$ssh -R <remote-port>:localhost:<local port to forward> <username>@host-to-connect-to
$ssh -R 10000:localhost:10000 ph0enix@10.2.3.85
```

## Proxychains
```
[Config] cat /etc/proxychains4.conf
[Config] socks5 localhost 1080

Now, that this is setup, anything that we want to proxify can be done with the prefix $proxychains nmap - etc..
[Note] proxychains bash #This should proxify the bash terminal
```


## Chisel (Windows)
```
TBD
```