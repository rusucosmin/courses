#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int p2c[2];
    int c2p[2];
    int cnt = 0;
    int i;
    /// [0] -> read
    /// [1] -> write
    pipe(p2c);
    pipe(c2p);
    if(fork() == 0) {
        close(p2c[1]);
        close(c2p[0]);
        char ch;
        while(read(p2c[0], &ch, sizeof(char)))
            if(strchr("aeiou", ch))
                ++ cnt;
        close(p2c[0]);
        write(c2p[1], &cnt, sizeof(int));
        close(c2p[1]);
        printf("Child got %d", cnt);
        exit(0);
    }
    close(p2c[0]);
    close(c2p[1]);
    char ch;
    while(scanf("%c", &ch) && ch != '\n')
        write(p2c[1], &ch, sizeof(char));
    close(p2c[1]);
    read(c2p[0], &cnt, sizeof(int));
    close(c2p[0]);
    printf("Parent received: %d\n", cnt);
    wait(0);
    return 0;
}
