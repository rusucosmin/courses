/*

Citesti un numar in procesul principal, il transmiti procesului fiu,
fiul, trimite parintelui valoarea 1 daca e par, sau 0 daca e impar.

*/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int n;
    int c2p[2], p2c[2];
    /// [0] - read
    /// [1] - write pipe(c2p);
    pipe(p2c);
    pipe(c2p);
    int res = fork();
    if(res < 0) {
        printf("Error fork()-ing\n");
        return 0;
    }
    if(res == 0) {
        close(p2c[1]);
        close(c2p[0]);
        read(p2c[0], &n, sizeof(int));
        close(p2c[0]);
        int packet = 1 - n % 2;
        write(c2p[1], &packet, sizeof(int));
        close(c2p[0]);
        exit(1);
    }
    scanf("%d", &n);
    close(p2c[0]);
    close(c2p[1]);
    write(p2c[1], &n, sizeof(int));
    close(p2c[1]);
    int response;
    read(c2p[0], &response, sizeof(int));
    close(c2p[0]);
    printf("Father received %d from child\n", response);
    wait(0);
    return 0;
}
