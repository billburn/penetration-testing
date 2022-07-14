# OS and Patch Enumeration

| Command	| Summary |
| --------- | ---------------------------- |
| systeminfo | Returns details about the system |
| systeminfo | findstr /b /c:"OS Name" /c:"OS Version" /c:"System Type"	| Returns only the fields OS version, name, and OS type |
| wmic qfe |Returns details about installed OS patches |
| wmic qfe get Caption,Description,HotFixID,InstalledOn | Returns only the fields Caption, Description, HotFxID, and InstallledOn |
| wmic logicaldisk | Returns all logicaldisk inforamtion |
| wmic logicaldisk get Caption,Description,ProviderName	| Returns on the fields Caption, Description, and ProviderName |