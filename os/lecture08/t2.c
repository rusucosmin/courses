#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void* func(void* p) {
    int i;
    for(i=0; i<5; i++) {
        printf("%u\n", pthread_self() % 10000);
        usleep(1);
    }
    return NULL;
}

int main() {
    int i;
    pthread_t t[3];

    for(i=0; i<3; i++) {
        pthread_create(&t[i], NULL, func, NULL);
    }

    for(i=0; i<5; i++) {
        printf("-\n");
        usleep(1);
    }

    for(i=0; i<3; i++) {
        pthread_join(t[i], NULL);
    }

    return 0;
}
