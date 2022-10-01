# Wfuzz Usage

## Wufzz Basic Usage
```
sudo wfuzz -c -f sub-fighter.txt -w subdomains-top1million-5000.txt -u 'http://cmess.thm' -H "Host:FUZZ.cmess.thm" --hw 290
```

[Bruteforcing Subdomains with Wfuzz](https://infinitelogins.com/2020/09/02/bruteforcing-subdomains-wfuzz/)