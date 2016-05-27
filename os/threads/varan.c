/*
6. Creezi un subproces care creeaza 10 threaduri si in thread se genereaza numere random pana cand is cel putin 5 intre 1-300, 5 intre 301-600, 5 intre 601-900, si la final trimiti cate s-au generat din fiecare in procesul principal prin fifo.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>

#define M 3
#define T 10

pthread_mutex_t mtx[M];
pthread_t t[T];
int cnt[M];

void* doIt(void *arg) {
    while(cnt[0] < 5 || cnt[1] < 5 || cnt[2] < 5) {
        int x = 1 + rand() % 900;
        printf("Thread: %d\n", x);
        if(x <= 300) {
            pthread_mutex_lock(&mtx[0]);
            cnt[0] ++;
            pthread_mutex_unlock(&mtx[0]);
        }
        else if(x <= 600) {
            pthread_mutex_lock(&mtx[1]);
            ++ cnt[1];
            pthread_mutex_unlock(&mtx[1]);
        }
        else {
            pthread_mutex_lock(&mtx[2]);
            ++ cnt[2];
            pthread_mutex_unlock(&mtx[2]);
        }
    }
    return NULL;
}

int main() {
    srand(time(NULL));
    int i;
    if(fork() == 0) {
        for(i = 0; i < M; ++ i)
            pthread_mutex_init(&mtx[i], NULL);
        for(i = 0; i < T; ++ i)
            pthread_create(&t[i], NULL, doIt, NULL);
        for(i = 0; i < T; ++ i)
            pthread_join(t[i], NULL);
        for(i = 0; i < M; ++ i)
            pthread_mutex_destroy(&mtx[i]);
        printf("Subprocess\n");
        int c2p = open("c2p", O_WRONLY);
        for(i = 0; i < M; ++ i) {
            printf("%d ", cnt[i]);
            write(c2p, &cnt[i], sizeof(int));
        }
        close(c2p);
        printf("\n");
        exit(0);
    }
    int c2p = open("c2p", O_RDONLY);
    for(i = 0; i < M; ++ i)
        read(c2p, &cnt[i], sizeof(int));
    close(c2p);
    printf("Main Process\n");
    for(i = 0; i < M; ++ i)
        printf("%d ", cnt[i]);
    printf("\n");
    wait(0);
    return 0;
}
