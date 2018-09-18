#include <stdio.h>
#include <pthread.h>

#define N 100

pthread_mutex_t mtxz;
pthread_mutex_t mtxo;

void* zero(void* p) {
    int k = 0;
    while(k < N) {
        pthread_mutex_lock(&mtxz);
        printf("zero\n");
        k++;
        pthread_mutex_unlock(&mtxo);
    }
    return NULL;
}
void* one(void* p) {
    int k = 0;
    while(k < N) {
        pthread_mutex_lock(&mtxo);
        printf("o\n");
        k++;
        pthread_mutex_unlock(&mtxz);
    }
    return NULL;
}

int main() {
    pthread_t z, o;

    pthread_mutex_init(&mtxz, NULL);
    pthread_mutex_init(&mtxo, NULL);

    pthread_mutex_lock(&mtxo);

    pthread_create(&z, NULL, zero, NULL);
    pthread_create(&o, NULL, one, NULL);

    pthread_join(z, NULL);
    pthread_join(o, NULL);

    pthread_mutex_destroy(&mtxz);
    pthread_mutex_destroy(&mtxo);

    return 0;
}
