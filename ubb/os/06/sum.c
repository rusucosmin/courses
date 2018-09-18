#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int a[4] = {1, 2, 3, 4};
    int c2p[2];

    pipe(c2p);

    if(fork() == 0) {
        a[2] += a[3];
        write(c2p[1], &a[2], sizeof(int));
        close(c2p[0]);
        close(c2p[1]);
        exit(0);
    }
    a[0] += a[1];
    wait(0);

    read(c2p[0], &a[2], sizeof(int));
    
    close(c2p[0]);
    close(c2p[1]);

    a[0] += a[2];

    printf("%d\n", a[0]);
    return 0;
}
