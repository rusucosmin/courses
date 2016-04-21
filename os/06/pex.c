#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int i, child;

    for(i=0; i<20; i++) {
        child = fork();
        if(child == 0) {
            printf("\n###########################################\n");
            if(execl("/bin/ps", "/bin/ps", "-f", NULL) == -1) {
                perror("Failed to do exec");
            }
            exit(0);
        }
    }
    for(i=0; i<20; i++) {
        wait(0);
    }

    return 0;
}
