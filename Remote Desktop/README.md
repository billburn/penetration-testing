# Remote Desktop

* In the past, I have used rdesktop extensively, but there are a number of certificate and TLS issues
* Use Remmina Remote Desktop Client

## Remmina
![Remmina](https://github.com/billburn/penetration-testing/blob/master/Remote%20Desktop/Images/remmina-01.png)

## Xfreerdp
```
xfreerdp /u:kkidd /size:80%hw /p:Pass123321@ /v:10.10.182.203 +clipboard
```