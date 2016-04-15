#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

struct Package {
    int pid;
    char result[100], arg[100];
}

int main(int argc, char ** argv) {
    int c2p[2][2];
    pipe(c2p[0]);
    pipe(c2p[1]);
    for(int i = 1 ; i < argc ; ++ i) { // ignore
        if(fork() == 0) {
            int check = system("test -f process.c");
            printf("First child %d\n", check);
            check = system("test -d process.c");
            printf("First child %d\n", check);
            /*FILE *f = popen("ls *", "r");
            char s[10000];
            fread(s, 1, sizeof(s), f);
            printf("First child %s\n", s);
            */
            exit(0);
        }
        if(fork() == 0) {
            FILE *f = popen("man man", "r");
            char s[100];
            fread(s, 1, sizeof(s), f);
            printf("Second child %s\n", s);
            exit(0);
        }
        printf("Parent: %s\n", argv[i]);
    }
    for(int i = 1 ; i < argc ; ++ i) {
        wait(0);
        wait(0);
    }
    return 0;
}
