## Fixing Terminal

```
which python
/usr/bin/python -c 'import pty; pty.spawn("/bin/bash")'
CTRL + Z  ## Backgrounds the Session
[RUN ON ATTACKING HOST] $ stty raw -echo
[RUN ON ATTACKING HOST] $ fg [ENTER] [ENTER]
[RUN ON ATTACKING HOST] $ stty -a (make note of the rows and cols)
$export TERM=xterm
$stty rows XX cols XX [ENTER]

[*] This should fix the terminal
```