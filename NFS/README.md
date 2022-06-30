# NFS

[URL] (https://linuxize.com/post/how-to-mount-an-nfs-share-in-linux/)

## Mount NFS
```
sudo mkdir /mnt/dev
sudo mount -t nfs 192.168.10.19:/srv/nfs /mnt/dev
```

## Unmounting NFS
```
sudo umount 192.168.10.19:/srv/nfs
sudo umount /mnt/dev (test this - might simply need to delete)
```