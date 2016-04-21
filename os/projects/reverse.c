#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    char s[10005];
    int c2p[2], p2c[2];
    pipe(c2p);
    pipe(p2c);
    if(fork() == 0) {
        read(p2c[0], s, sizeof(s));
        int i, n = strlen(s);
        for(i = 0 ; i < n / 2 ; ++ i) {
            char aux = s[i];
            s[i] = s[n - i - 1];
            s[n - i - 1] = aux;
        }
        write(c2p[1], s, sizeof(s));
        exit(1);
    }
    fgets(s, sizeof(s), stdin);
    close(p2c[0]);
    close(c2p[1]);
    write(p2c[1], s, sizeof(s));
    close(p2c[1]);
    read(c2p[0], s, sizeof(s));
    printf("%s\n", s);
    close(c2p[0]);
    wait(0);
    return 0;
}
