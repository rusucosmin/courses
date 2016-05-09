/*
2. Write a program that creates threads and increments a global variable n=0 with the values from a struct given as argument to each thread until it is greater than 20. The struct contains for each thread 2 random numbers generated in the main program.
*/

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <pthread.h>

#define T 10
#define maxrand 100
#define maxn 1000

int n;
pthread_mutex_t mtx;

struct pair {
    int first, second;
};

void* run(void *arg) {
    struct pair * act = (struct pair *) arg;
    printf("Thread has %d and %d. n = %d\n", act->first, act->second, n);
    while(n < maxn) {
        pthread_mutex_lock(&mtx);
        printf("Thread n = %d + %d\n", n, act->first);
        n += act->first;
        pthread_mutex_unlock(&mtx);
        if(n < maxn) {      /// so that once it is greater, then it is no need to increment again with the second generated random number
            pthread_mutex_lock(&mtx);
            printf("Thread n = %d + %d\n", n, act->second);
            n += act->second;
            pthread_mutex_unlock(&mtx);
        }
    }
    free(act);
    return NULL;
}

int main() {
    srand(time(NULL));

    int i;
    pthread_t t[T];
    pthread_mutex_init(&mtx, NULL);
    for(i = 0 ; i < T ; ++ i) {
        struct pair * act = (struct pair *)malloc(sizeof(struct pair));
        act->first = rand() % maxrand;
        act->second = rand() % maxrand;
        pthread_create(&t[i], NULL, run, (void *)act);
    }

    for(i = 0 ; i < T ; ++ i) {
        pthread_join(t[i], NULL);
    }
    printf("%d\n", n);
    pthread_mutex_destroy(&mtx);
    return 0;
}
