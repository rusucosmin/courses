/*

For each command line argument launch two subprocesses that will race to establish:
- the length of the longest line, if the argument is a file (using popen and wc).
- the size in bytes if the argument is a directory (using popen and du). 
Each process, before send the result to the parent, will sleep between one and five seconds (using sleep call).
The communication between processes we will use a single pipe channel.
Each process will send to the parent a structure that contains his pid, the argument and the established result.
The parent will print only the n/2 received results (n being the number of arguments), the rest will be ignored.

*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <time.h>

typedef struct {
    int pid;
    char result[100], arg[100];
} Package;

int main(int argc, char ** argv) {
    srand(time(NULL));
    int c2p[2][2];
    pipe(c2p[0]);
    pipe(c2p[1]);
    int i, j;
    for(i = 1 ; i < argc ; ++ i) {
        for(j = 0 ; j < 2 ; ++ j) {
            if(fork() == 0) {
                /// the son only writes (1)
                close(c2p[j][0]);               /// close the actual child's read pipe
                close(c2p[1 - j][0]);           /// close the other child's pipe
                close(c2p[1 - j][1]);           /// both of them
                char cmd[1000];
                strcpy(cmd, "test -f ");
                strcat(cmd, argv[i]);
                int check = system(cmd);        /// run test -f and get the resul (0 -> true, != 0 ->false);
                Package p;
                p.pid = getpid();
                strcpy(p.arg, argv[i]);
                if(check == 0) {
                    strcpy(cmd, "wc -L ");
                    strcat(cmd, argv[i]);
                    FILE *f;
                    f = popen(cmd, "r");
                    fgets(p.result, sizeof(p.result), f);
                    sleep(rand() % 5);
                    write(c2p[j][1], &p, sizeof(Package));
                }
                else {
                    strcpy(cmd, "test -d ");
                    strcat(cmd, argv[i]);
                    check = system(cmd);
                    if(check == 0) {
                        strcpy(cmd, "du -s ");
                        strcat(cmd, argv[i]);
                        FILE *f;
                        f = popen(cmd, "r");
                        fgets(p.result, sizeof(p.result), f);
                        sleep(rand() % 5);
                        write(c2p[j][1], &p, sizeof(Package));
                    }
                    else {
                        strcpy(p.result, "The arg is not a file, neither a directory");
                        sleep(rand() % 5);
                        write(c2p[j][1], &p, sizeof(Package));
                    }
                }
                close(c2p[j][1]);
                exit(0);
            }
        }
    }
    for(i = 1 ; i <= argc / 2 ; ++ i)
        for(j = 0 ; j < 2 ; ++ j) {
            Package p;
            read(c2p[j][0], &p, sizeof(Package));
            p.result[strlen(p.result) - 1] = '\0';
            printf("Father received:\nPid = %d\nResult = %s\nCmd = %s\n\n", p.pid, p.result, p.arg);
        }
    close(c2p[0][0]);
    close(c2p[0][1]);
    close(c2p[1][0]);
    close(c2p[1][1]);
    for(i = 1 ; i <= argc ; ++ i) {
        for(j = 0 ; j < 2 ; ++ j) {
            wait(0);
        }
    }
    return 0;
}
