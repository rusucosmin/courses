#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
    int n, pa, ab, bp;
    if(fork() == 0) {
        pa = open("pa", O_RDONLY);
        ab = open("ab", O_WRONLY);

        do {
            read(pa, &n, sizeof(int));
            if(n % 2 == 0)
                n /= 2;
            write(ab, &n, sizeof(int));
        }while(n > 100);

        close(pa);
        close(ab);
        exit(0);
    }
    if(fork() == 0) {
        ab = open("ab", O_RDONLY);
        bp = open("bp", O_WRONLY);

        do {
            read(ab, &n, sizeof(int));
            if(n % 3 == 0)
                n /= 3;
            write(bp, &n, sizeof(int));
        }while(n > 100);

        close(ab);
        close(bp);
        exit(0);
    }
    pa = open("pa", O_WRONLY);
    bp = open("bp", O_RDONLY);
    scanf("%d", &n);
    do {
        write(pa, &n, sizeof(int));
        read(bp, &n, sizeof(int));
        printf("Father: %d\n", n);
        n -= 5;
    } while(n > 100);
    close(pa);
    close(bp);
    wait(0);
    wait(0);
    return 0;
}
