# RPCCLient

## Null Session Login
```
$rpcclient -U "" -N 192.168.10.14
```

## Enumerate Users
```
rpclient $> enumdomusers
rpclient $> querydispinfo[2,3]
```

## Enumerate Single Users
```
rpcclient $> queryuser <username>
```