#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

int main() {
    printf("A START %d\n", getpid());
    execl("./p2b", "./p2b", NULL);
    printf("A STOP %d\n", getpid());
    return 0;
}
