#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

int main() {
    int ball = 1;
    int a2b, b2a;

    if(fork() == 0) {
        a2b = open("a2b", O_WRONLY);
        b2a = open("b2a", O_RDONLY);
        while(ball < 10) {
            read(b2a, &ball, sizeof(int)); printf("A: %d\n", ball);
            ball++; write(a2b, &ball, sizeof(int));
        }
        close(a2b); close(b2a); exit(0);
    }

    if(fork() == 0) {
        a2b = open("a2b", O_RDONLY);
        b2a = open("b2a", O_WRONLY);
        while(ball < 10) {
            read(a2b, &ball, sizeof(int)); printf("B: %d\n", ball);
            ball++; write(b2a, &ball, sizeof(int));
        }
        close(a2b); close(b2a); exit(0);
    }

    b2a = open("b2a", O_WRONLY);
    write(b2a, &ball, sizeof(int));

    wait(0); wait(0);

    close(b2a);
    return 0;
}
