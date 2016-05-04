#include <stdio.h>
#include <pthread.h>

#define N 1000

pthread_mutex_t mtx;

int turn = 0;

void* zero(void* p) {
    int k = 0;
    while(k < N) {
        pthread_mutex_lock(&mtx);
        if(turn == 0) {
            printf("zero\n");
            turn = 1;
            k++;
        }
        pthread_mutex_unlock(&mtx);
    }
    return NULL;
}

void* one(void* p) {
    int k = 0;
    while(k < N) {
        pthread_mutex_lock(&mtx);
        if(turn == 1) {
            printf("o\n");
            turn = 0;
            k++;
        }
        pthread_mutex_unlock(&mtx);
    }
    return NULL;
}

int main() {
    pthread_t z, o;

    pthread_mutex_init(&mtx, NULL);

    pthread_create(&z, NULL, zero, NULL);
    pthread_create(&o, NULL, one, NULL);

    pthread_join(z, NULL);
    pthread_join(o, NULL);

    pthread_mutex_destroy(&mtx);

    return 0;
}

