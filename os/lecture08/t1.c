#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void* func(void* p) {
    int i;
    for(i=0; i<5; i++) {
        printf("T\n");
        usleep(200000);
    }
    return NULL;
}

int main() {
    int i;
    pthread_t t;

    pthread_create(&t, NULL, func, NULL);

    for(i=0; i<5; i++) {
        printf("-\n");
        usleep(200000);
    }

    pthread_join(t, NULL);

    return 0;
}
