# GNUPG

## Stealing Private Key / Cracking Hash
```
* If you come across .asc with a private key, but no password.  Copy the private key down with ncat or similiar
$gpg2john <private-key.asc> > private-key.hash
$john --wordlist:/usr/share/rockyou.txt private-key.hash
```

## Importing Private Key
```
* Make sure you have the private key imported or else you wont be able to read the pgp encrypted file
$gpg --import tryhackme.asc
```

## Decrypting File
```
$gpg -d credential.pgp                                       
                                                                             
You need a passphrase to unlock the secret key for       
<passphrase for private-key.hash>
```