/*
Sa se implementeze un proces care creeaza un proces fiu cu care comunica
prin pipe. Procesul parinte trimite prin pipe procesului fiu doua numere
intregi iar fiul returneaza prin pipe suma lor.
*/

#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    int a, b, sum;
    int c2p[2], p2c[2];
    pipe(c2p);
    pipe(p2c);
    int res = fork();
    /// [0] - read
    /// [1] - write
    if(res < 0) {
        printf("Error forking\n");
        return 0;
    }
    if(res == 0) {
        close(p2c[1]);
        close(c2p[0]);
        read(p2c[0], &a, sizeof(int));
        read(p2c[0], &b, sizeof(int));
        close(p2c[0]);
        sum = a + b;
        write(c2p[1], &sum, sizeof(int));
        close(c2p[1]);
        exit(0);
    }
    close(p2c[0]);
    close(c2p[1]);
    scanf("%d%d", &a, &b);
    write(p2c[1], &a, sizeof(int));
    write(p2c[1], &b, sizeof(int));
    close(p2c[1]);
    read(c2p[0], &sum, sizeof(int));
    close(c2p[0]);
    printf("Sum: %d\n", sum);
    wait(0);
    return 0;
}
