# RPCCLient

## Null Session Login
```
$rpcclient -U '' <ipaddress>
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