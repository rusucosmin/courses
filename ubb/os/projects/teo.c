#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int c2c[2][2], c2p[2][2], id0, id1, x;
    pipe(c2c[0]); /// c0 to c1
    pipe(c2c[1]); /// c1 to c0
    pipe(c2p[0]); /// c0 to p
    pipe(c2p[1]); /// c1 to p
    /// read (0)
    /// write (1)
    if(fork() == 0) {
        /// child0 writes(1) to child1 it's pid
        /// child1 reads(0) from child2 it's pid
        close(c2c[0][0]);
        close(c2p[1][0]); /// close read c1->p
        close(c2p[1][1]); /// close write c1->p
        close(c2c[1][1]);
        close(c2p[0][0]);
        id0 = getpid();
        write(c2c[0][1], &id0, sizeof(int));
        close(c2c[0][1]);
        read(c2c[1][0], &id1, sizeof(int));
        close(c2c[1][0]);
        x = id0 % id1;
        write(c2p[0][1], &x, sizeof(int));
        close(c2p[0][1]);
        printf("First child: %d %d\n", id0, id1);
        exit(0);
    }
    if(fork() == 0) {
        /// child1 reads(0) from child0 it's pid
        /// child1 writes(1) to child0 it's pid
        /// send them to parent
        id1 = getpid();
        close(c2p[0][0]);
        close(c2p[0][1]);
        close(c2p[1][0]);
        close(c2c[0][1]);
        close(c2c[1][0]);
        read(c2c[0][0], &id0, sizeof(int));
        close(c2c[0][0]);
        write(c2c[1][1], &id1, sizeof(int));
        close(c2c[1][1]);
        x = id1 % id0;
        write(c2p[1][1], &x, sizeof(int));
        close(c2p[1][1]);
        printf("Second child: %d %d\n", id0, id1);
        exit(0);
    }
    close(c2c[0][0]);
    close(c2c[0][1]);
    close(c2c[1][0]);
    close(c2c[1][1]);
    close(c2p[0][1]);
    close(c2p[1][1]);

    int c0, c1;
    read(c2p[0][0], &c0, sizeof(int));
    read(c2p[1][0], &c1, sizeof(int));
    printf("Father received from first child: %d and from second child: %d\n", c0, c1);

    close(c2p[0][0]);
    close(c2p[1][0]);
    wait(0);
    wait(0);
    return 0;
}
