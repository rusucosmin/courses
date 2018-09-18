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
