/*
1. Implement a program that writes a number between 0 and 9 in a global variable and then creates 10 threads.
Each thread will check the global variable and if its value is the order number of the thread (given from
main at creation time), the thread writes in the global variable another number between 0 and 9 (different
than its own). The program ends when the global variable is changed 20 times.
*/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <pthread.h>

#define T 10
#define STOP 20

int var, cnt;
pthread_mutex_t mtx;

int randT() {
    return rand() % T;
}

int randTexc(int i) {
    int x = randT();
    while(x == i)
        x = randT();
    return x;
}

void* doIt(void* arg) {
    int id = *(int*)arg;
    while(cnt < STOP) {
        pthread_mutex_lock(&mtx);
        if(var == id && cnt < STOP) {
            var = randTexc(id);
            printf("%d: Thread %d: var = %d\n", cnt, id, var);
            ++ cnt;
        }
        pthread_mutex_unlock(&mtx);
    }
    free(arg);
    return NULL;
}

int main() {
    pthread_t t[T];
    int i;
    srand(time(NULL));
    var = randT();
    printf("Initially var = %d\n", var);
    pthread_mutex_init(&mtx, NULL);
    for(i = 0; i < T; ++ i) {
        int* x = (int*) malloc(sizeof(int));
        *x = i;
        pthread_create(&t[i], NULL, doIt, (void*) x);
    }

    for(i = 0; i < T; ++ i) {
        pthread_join(t[i], NULL);
    }
    pthread_mutex_destroy(&mtx);
    return 0;
}
