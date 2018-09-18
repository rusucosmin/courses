#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 10
#define T 10

void* f(void* p) {
    int k = (int)p;
    int i;
    for(i=0; i<N; i++) {
        printf("%d\n", k);
    }
    return NULL;
}

int main() {
    int i;
    pthread_t t[T];

    for(i=0; i<T; i++) {
        pthread_create(&t[i], NULL, f, (void*)i);
    }

    for(i=0; i<N; i++) {
        printf("M\n");
    }

    for(i=0; i<T; i++) {
        pthread_join(t[i], NULL);
    }
    return 0;
}
