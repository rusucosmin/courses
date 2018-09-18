#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int ball = 1;
    int a2b[2], b2a[2];

    pipe(a2b);
    pipe(b2a);

    if(fork() == 0) {
        while(ball < 10) {
            read(b2a[0], &ball, sizeof(int));
            printf("A: %d\n", ball);
            ball++;
            write(a2b[1], &ball, sizeof(int));
        }
        close(a2b[0]); close(a2b[1]); close(b2a[0]); close(b2a[1]);
        exit(0);
    }

    if(fork() == 0) {
        while(ball < 10) {
            read(a2b[0], &ball, sizeof(int));
            printf("B: %d\n", ball);
            ball++;
            write(b2a[1], &ball, sizeof(int));
        }
        close(a2b[0]); close(a2b[1]); close(b2a[0]); close(b2a[1]);
        exit(0);
    }

    write(b2a[1], &ball, sizeof(int));
    wait(0); wait(0);

    close(a2b[0]); close(a2b[1]); close(b2a[0]); close(b2a[1]);
    return 0;
}
