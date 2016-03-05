#include <stdio.h>
#include <pthread.h>

#define N 100000


void* f1(void* p) {
    int i;
    for(i=0; i<N; i++) {
        printf("1\n");
    }
    return NULL;
}

void* f2(void* p) {
    int i;
    for(i=0; i<N; i++) {
        printf("2\n");
    }
    return NULL;
}

int main() {
    int i;
    pthread_t t1, t2;

    pthread_create(&t1, NULL, f1, NULL);
    pthread_create(&t2, NULL, f2, NULL);

    for(i=0; i<N; i++) {
        printf("M\n");
    }

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    return 0;
}
