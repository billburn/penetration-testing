# Port Forwarding

## Local
```
$ssh -L <remote-port>:localhost:<local port to forward> <username>@host-to-connect-to
$ssh -L 10000:localhost:10000 ph0enix@10.2.3.85
```

## Remote
```
$ssh -R <remote-port>:localhost:<local port to forward> <username>@host-to-connect-to
$ssh -R 10000:localhost:10000 ph0enix@10.2.3.85
```

## Chisel (Windows)
```
TBD
```