#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int i, child, sum=0;

    for(i=0; i<5; i++) {
        child = fork();
        if(child == 0) {
            sum += getpid();
            printf("Child %d sum %d\n", getpid(), sum);
            exit(0);
        }
        sum = i;
        printf("Parent created %d sum %d\n", child, sum);
    }
    for(i=0; i<5; i++) {
        wait(0);
    }

    sleep(10);

    return 0;
}
