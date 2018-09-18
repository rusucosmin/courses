#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N 10
#define T 10

void* f(void* p) {
    int k = *(int*)p;
    int i;
    for(i=0; i<N; i++) {
        printf("%d\n", k);
    }
    free(p);
    return NULL;
}

int main() {
    int i, *p;
    pthread_t t[T];

    for(i=0; i<T; i++) {
        p = (int*)malloc(sizeof(int));
        *p = i;
        pthread_create(&t[i], NULL, f, p);
    }

    for(i=0; i<N; i++) {
        printf("M\n");
    }

    for(i=0; i<T; i++) {
        pthread_join(t[i], NULL);
    }
    return 0;
}
