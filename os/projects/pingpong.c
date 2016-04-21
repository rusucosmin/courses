#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    int p2c[2], c2p[2];
    pipe(p2c);
    pipe(c2p);
    char c = 'a';
    /// [0] -> read
    /// [1] -> write
    if(fork() == 0) {
        close(p2c[1]);
        close(c2p[0]);
        while(1) {
            read(p2c[0], &c, sizeof(char));
            printf("Child: %c\n", c);
            c -= 'a';
            c ++;
            c = c % 26;
            c += 'a';
            write(c2p[1], &c, sizeof(char));
           }
        exit(0);
    }
    close(p2c[0]);
    close(c2p[1]);
    while(1) {
        sleep(rand() % 2);
        write(p2c[1], &c, sizeof(char));
        read(c2p[0], &c, sizeof(char));
        printf("Dad: %c\n", c);
    }
    wait(0);
    return 0;
}
