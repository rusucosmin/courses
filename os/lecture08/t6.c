#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define T 1000
#define N 1000000

int counter = 0;
pthread_mutex_t mtx;

void* f(void* p) {
    int i;

    for(i=0; i<N; i++) {
        pthread_mutex_lock(&mtx);
        counter++;
        pthread_mutex_unlock(&mtx);
    }
    return NULL;
}

int main() {
    int i;
    pthread_t t[T];

    pthread_mutex_init(&mtx, NULL);

    for(i=0; i<T; i++) {
        pthread_create(&t[i], NULL, f, NULL);
    }

    for(i=0; i<T; i++) {
        pthread_join(t[i], NULL);
    }
    printf("%d\n", counter);

    pthread_mutex_destroy(&mtx);
    return 0;
}
