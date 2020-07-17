# Webdav Testing

## Davtest

```
$davtest -url http://url-of-the-host
```

## Davtest through proxy

```
Open Burp
Setup new proxy listener
Set local listener port *(80) 
Set remote host (10.10.10.15)
Set remote port (80)
```

## Setting up proxy 

![Davtest-01](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-01.png)

## Confirming Webdav Manipulation

![Davtest-02](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-02.png)

## Davtest

![Davtest-03](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-03.png)

## Test upload using post

```
1) Send one of the PUT request to the repeater tab
2) Modify the URL to /test.html or whatever you like
3) In the body add some text and send the request; you should get a 200 
```

![Davtest-04](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-04.png)

![Davtest-05](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-05.png)