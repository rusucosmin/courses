#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int i, p;
    char* cmd[] = {"./p2bq", "/bin/ls", "/bin/ps"};

    printf("Parent START\n");
    for(i=0; i<3; i++) {
        p = fork();
        if(p == 0) {
            if(execl(cmd[i], cmd[i], NULL) < 0) {
                perror("Exec failed");
            }
            exit(0);
        }
    }

    printf("Parent MIDDLE\n");

    for(i=0; i<3; i++) {
        wait(0);
    }
    printf("Parent END\n");

    return 0;
}
