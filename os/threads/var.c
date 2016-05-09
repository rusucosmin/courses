/**
1.  Write a program that creates 4 threads and had 3 global variables v5, v2, v3. Each thread generates a random number and:
    - if the number is multiple of 2 increments v2
    - if the number is multiple of 3 increments v3
    - if the number is multiple of 5 increments v5

    The number can be a multiple of more numbers (ex. for 10 we will increment both V2 and V5). Threads print the generated numbers and stop when 30 numbers have been generated. The main program prints the 3 global variables.
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define T 4
#define var 3
#define cnt 5

int v[var];
pthread_mutex_t mtx;

void* incVars(void *arg) {
    int i;
    for(i = 0 ; i < cnt ; ++ i) {
        int x = rand();
        pthread_mutex_lock(&mtx);
        printf("Thread %lld generated %d\n", (long long)pthread_self(), x);
        printf("So the values are: %d %d %d\n", x % 2, x % 3, x % 5);
        pthread_mutex_unlock(&mtx);
        if(x % 2 == 0) {
            pthread_mutex_lock(&mtx);
            ++ v[0];
            pthread_mutex_unlock(&mtx);
        }
        if(x % 3 == 0) {
            pthread_mutex_lock(&mtx);
            ++ v[1];
            pthread_mutex_unlock(&mtx);
        }
        if(x % 5 == 0) {
            pthread_mutex_lock(&mtx);
            ++ v[2];
            pthread_mutex_unlock(&mtx);
        }
    }
    return NULL;
}

int main() {
    srand(time(NULL));

    pthread_t t[T];
    int i;
    pthread_mutex_init(&mtx, NULL);
    for(i = 0 ; i < T ; ++ i) {
        pthread_create(&t[i], NULL, incVars, NULL);
    }
    for(i = 0 ; i < T ; ++ i) {
        pthread_join(t[i], NULL);
    }
    for(i = 0 ; i < var ; ++ i) {
        printf("%d ", v[i]);
    }
    printf("\n");
    pthread_mutex_destroy(&mtx);
    return 0;
}
