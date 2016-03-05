#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    printf("B %d\n", getpid());
    return 0;
}
