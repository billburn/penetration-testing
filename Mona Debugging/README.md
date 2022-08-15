# Mona.py Helpful Commands

| Command | Summary |
| ---------------------------- | ---------------------------- |
| Set working directory | ```!mona config -set workingfolder c:\mona-working-dir``` |
| Pattern Created | ```!mona pattern_create 3000```  |
| Pattern Offset (EIP or ASCII) | ```!mona pattern_offset EIP_VALUE ``` |
| Generate Byte Array | ```!mona bytearray -cpb "\x00"``` |
| Check for Bad Chars | ```!mona compare -f c:\mona-working-dir\bytearray.bin -a <EIP> address``` |