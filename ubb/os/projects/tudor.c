#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    int n, i, j;
    int p[3][2], mod[2] = {2, 3};
    for(i = 0 ; i < 3 ; ++ i)
        pipe(p[i]);
    for(i = 0 ; i < 2 ; ++ i)
        if(fork() == 0) {
            int from = i;
            int to = i + 1;
            for(j = 0 ; j < 3 ; ++ j) {
                if(j != from)
                    close(p[j][0]);
                if(j != to)
                    close(p[j][1]);
            }
            do {
                read(p[from][0], &n, sizeof(int));
                //printf("Child #%d: reads: %d ", i + 1, n);
                if(n % mod[i] == 0)
                    n /= mod[i];
                //printf("writes %d\n", n);
                write(p[to][1], &n, sizeof(int));
            } while(n > 100);
            close(p[from][0]);
            close(p[to][1]);
            exit(0);
        }
    scanf("%d", &n);
    int from = 2;
    int to = 0;
    for(i = 0 ; i < 3 ; ++ i) {
        if(i != from)
            close(p[i][0]);
        if(i != to)
            close(p[i][1]);
    }
    do {
        //printf("Father sends: %d\n", n);
        write(p[to][1], &n, sizeof(int));
        read(p[from][0], &n, sizeof(int));
        n -= 5;
        printf("Father : %d\n", n);
    } while(n > 100);
    close(p[to][1]);
    close(p[from][0]);
    wait(0);
    wait(0);
    return 0;
}
