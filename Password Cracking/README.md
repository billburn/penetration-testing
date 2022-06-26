# Password Cracking

## Make Passwords

- sha-256
```
openssl passwd -5 
Enter password at the prompt: P@ssw0rd123
$5$wAkFuhD7zT9ZQMFS$0Sa9s6aaQBLaXFXto9FdUoiy8Gw7FuMBQPAHvyJzjOB
```

- sha-512
```
openssl passwd -6
Enter password at the prompt: P@ssw0rd123
$6$klHi1Tjk3xO7Gk2F$qVfbmPZ1sLfqVIXnLG7Dn0Mdxnrd.eT3NC5ZuQR0/YNdyl.kFC42NU7VJQ2uhKPlG1nC4PI5YE72BBKCeLmBX0
```