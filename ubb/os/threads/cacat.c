/*
1. *Suciu* Sa se scrie un program care primeste ca si argumente nume de programe urmate de argumente. Numele unui program este de separat de ultimul argument al progrmaului precedent prin -. Programul va rula programele primilte ca argumente cu parametrii corespunzatori in procese fiu simultane folosing apelurile sistem exec. In cazul in care apelul exec esaueaza, se va raporta un mesaj de eroare si codul de eroare.
Ex: `./aprog /bin/ls /etc - /esr/bin/wc /etc/passwd - /bin/grep aa /etc/passwd`
    - **FILE: `cacat.c`**
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>

void doBullshit(int argc, char **argv) {
    if(!argc) {
        printf("N-am foita sa rulez...\n");
        return ;
    }
    printf("%s\n\n", argv[0]);
    argv[argc] = NULL;
    if(execv(argv[0], argv) == -1)
        printf("Shit happeded: %d\n", errno);
}

int main(int argc, char ** argv) {
    int i, act = 0, cnt = 0;
    char **cmd;
    cmd = (char **) malloc(argc * sizeof(char *));
    for(i = 1; i < argc; ++ i) {
        if(!strcmp(argv[i], "-")) {
            ++ cnt;
            if(fork() == 0) {
                doBullshit(act, cmd);
                exit(0);
            }
            act = 0;
        }
        else
            cmd[act ++] = argv[i];
    }
    ++ cnt;
    if(fork() == 0) {
        doBullshit(act, cmd);
        exit(0);
    }
    free(cmd);
    for(i = 0; i < cnt; ++ i)
        wait(0);
    return 0;
}
