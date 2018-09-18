#include <stdio.h>
#include <pthread.h>

void* func(void* arg) {
    printf("%u\n", pthread_self()); // ~= getpid()
    return NULL;
}

int main() {
    pthread_t tid[3];
    int i;

    for(i=0; i<3; i++) {
        pthread_create(&tid[i], NULL, func, NULL);
    }

    for(i=0; i<3; i++) {
        pthread_join(tid[i], NULL);
    }

    return 0;
}
