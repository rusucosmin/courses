/*
Implement a program that writes a number between 0 and 9 in a global variable and then creates 10 threads.
Each thread will check the global variable and if its value is the order number of the thread (given from
main at creation time), the thread writes in the global variable another number between 0 and 9 (different
than its own). The program ends when the global variable is changed 20 times.
*/

#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#define N 10000
#define T 100

pthread_t tid[T];
pthread_mutex_t mtx;

int cnt;

void * func(void *arg) {
    int i;
    for(i = 0; i < N; ++ i) {
        pthread_mutex_lock(&mtx);
        cnt ++;
        pthread_mutex_unlock(&mtx);
    }
    return NULL;
}

int main() {
    int i;
    pthread_mutex_init(&mtx, NULL);
    for(i = 0; i < T; ++ i)
        pthread_create(&tid[i], NULL, func, NULL);
    for(i = 0; i < T; ++ i)
        pthread_join(tid[i], NULL);
    printf("%d\n", cnt);
    pthread_mutex_destroy(&mtx);
    return 0;
}
