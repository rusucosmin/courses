#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int i, p;

    for(i=0; i<5; i++) {
        p = fork();
        if(p == 0) {
            exit(0);
        }
    }

    sleep(10);

    for(i=0; i<5; i++) {
        wait(0);
    }

    return 0;
}
