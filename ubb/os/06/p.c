#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int i, child, sum=0;

    for(i=0; i<20; i++) {
        child = fork();
        if(child == 0) {
            sum += 1;
            printf("Child %d sum %d\n", i, sum);
            exit(0);
        }
    }
    for(i=0; i<20; i++) {
        wait(0);
    }
    printf("Parent sum %d\n", sum);

    return 0;
}
