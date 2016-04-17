#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

typedef struct {
    int pid;
    char result[100], arg[100];
} Package;

int main(int argc, char ** argv) {
    int c2p[2][2];
    pipe(c2p[0]);
    pipe(c2p[1]);
    for(int i = 1 ; i < argc ; ++ i) { // ignore
        for(int j = 0 ; j < 2 ; ++ j) {
            if(fork() == 0) {
                /// the son only writes (1)
                close(c2p[j][0]);           /// close the actual child's read pipe
                close(c2p[1 - j][0]);         /// close the other child's pipe
                close(c2p[1 - j][1]);         /// both of them
                char cmd[1000];
                strcpy(cmd, "test -f ");
                strcat(cmd, argv[i]);
                int check = system(cmd);
                Package p;
                p.pid = getpid();
                strcpy(p.arg, argv[i]);
                if(check == 0) {
                    strcpy(cmd, "wc -L ");
                    strcat(cmd, argv[i]);
                    FILE *f = popen(cmd, "r");
                    fread(p.result, 1, sizeof(p.result), f);
                    p.result[strlen(p.result)] = '\0';
                    write(c2p[j][1], &p, sizeof(Package));
                }
                else {
                    strcpy(cmd, "test -d ");
                    strcat(cmd, argv[i]);
                    check = system(cmd);
                    if(check == 0) {
                        strcpy(cmd, "du -s ");
                        strcat(cmd, argv[i]);
                        FILE *f = popen(cmd, "r");
                        fread(p.result, 1, sizeof(p.result), f);
                        p.result[strlen(p.result)] = '\0';
                        write(c2p[j][1], &p, sizeof(Package));
                    }
                    else {
                        strcpy(p.result, "The arg is not a file, neither a directory");
                        p.result[strlen(p.result)] = '\0';
                        write(c2p[j][1], &p, sizeof(Package));
                    }
                }
                close(c2p[j][1]);
                exit(0);
            }
        }
    }
    for(int i = 1 ; i < argc ; ++ i)
        for(int j = 0 ; j < 2 ; ++ j) {
            Package p;
            read(c2p[j][0], &p, sizeof(Package));
            p.result[strlen(p.result)] = '\0';
            p.arg[strlen(p.arg)] = '\0';
            printf("Father received:\nPid = %d\nResult = %s\nCmd = %s\n\n", p.pid, p.result, p.arg);
            sleep(2);
        }
    close(c2p[0][0]);
    close(c2p[0][1]);
    close(c2p[1][0]);
    close(c2p[1][1]);
    for(int i = 1 ; i < argc ; ++ i) {
        for(int j = 0 ; j < 2 ; ++ j) {
            wait(0);
        }
    }
    return 0;
}
