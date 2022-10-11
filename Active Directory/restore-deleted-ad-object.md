# Restore Deleted AD Object

## Restore Deleted Object from AD using AD Recyle Bin

[Power Admin Article on Restoring AD Objects](https://www.poweradmin.com/blog/restoring-deleted-objects-from-active-directory-using-ad-recycle-bin/)

```
Get-ADForest
Get-ADOptionalFeature -Filter *
Enable-ADOptionalFeature -Identity 'Recycle Bin Feature' -Scope ForestOrConfigurationSet -Target 'cascade.local' -Server CASC-DC1
- ## Need to press 'Y' enter to proceed
Get-ADObject -filter 'isdeleted -eq $true -and name -ne "Deleted Objects"' -includeDeletedObjects -property *
Get-AdObject -Filter {DisplayName -like 'TempAdmin'} -IncludeDeletedObjects | Restore-ADObject
```