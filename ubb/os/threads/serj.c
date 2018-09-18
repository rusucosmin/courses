/*
3. Implement a program that creates two threads. The threads will print their ID (pthread_self) 10 times and then
stop. Insure that the printed IDs alternate always (ie A, B, A, B, ...)
*/
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

pthread_mutex_t mta, mtb;
pthread_t a, b;

void* funca(void *arg) {
    int i;
    for(i = 0; i < 10; ++ i) {
        pthread_mutex_lock(&mta);
        printf("Thread A = %d\n", (int)pthread_self());
        pthread_mutex_unlock(&mtb);
    }
    return NULL;
}

void* funcb(void *arg) {
    int i;
    for(i = 0; i < 10; ++ i) {
        pthread_mutex_lock(&mtb);
        printf("Thread B = %d\n", (int)pthread_self());
        pthread_mutex_unlock(&mta);
    }
    return NULL;
}

int main() {
    pthread_mutex_init(&mta, NULL);
    pthread_mutex_init(&mtb, NULL);

    pthread_mutex_lock(&mtb);

    pthread_create(&a, NULL, funca, NULL);
    pthread_create(&b, NULL, funcb, NULL);

    pthread_join(a, NULL);
    pthread_join(b, NULL);

    pthread_mutex_destroy(&mta);
    pthread_mutex_destroy(&mtb);
    return 0;
}
