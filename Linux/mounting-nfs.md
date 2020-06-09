#NFS

## Mounting NFS on Linux
```
sudo mkdir /mnt/kenobinfs                                                                                                                                          
sudo mount 10.10.150.166:/var /mnt/kenobinfs 
ls /mnt/kenobi

sudo mount -t nfs 10.10.19.240:/opt/files /mnt/files/
```