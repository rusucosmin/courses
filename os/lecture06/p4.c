#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int p;
    int a[] = {1, 2, 3, 4};
    int c2p[2];

    pipe(c2p);

    p = fork();
    a[0] += a[1];
    if(p == 0) {
        a[2] += a[3];
        write(c2p[1], &a[2], sizeof(int));
        exit(0);
    }

    wait(0);

    read(c2p[0], &a[2], sizeof(int));

    a[0] += a[2];

    printf("%d\n", a[0]);
    return 0;
}
