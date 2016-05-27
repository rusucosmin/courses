/*
5. Faci 10 procese. din fiecare 2 threaduri. fiecare thread genereaza random numere, si adauga la o suma threadurile genereaza alternativ t1, t2, t1, t2 pana cand ai generat 10 numere in total. si dupa aia, din subproces trimiti inapoi o structura care contine suma si pid-ul. mainul scrie PID-ul si suma procesului care a facut max
*/
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#include <pthread.h>
#include <sys/stat.h>
#include <fcntl.h>


#define P 10
#define T 2

int sum;
pthread_mutex_t mtx, mt[2];
pthread_t t[T];

struct package {
    pid_t pid;
    int sum;
};

void* doIt(void *arg) {
    int i, id = *(int *)arg;
    for(i = 0; i < 5; ++ i) {
        pthread_mutex_lock(&mt[id]);
        int x = rand() % 100;
        sum += x;
        pthread_mutex_unlock(&mt[1 - id]);
    }
    free(arg);
    return NULL;
}


int main() {
    int i;
    for(i = 0; i < P; ++ i)
        if(fork() == 0) {
            srand(time(NULL) ^ (getpid()<<16));
            int j;
            pthread_mutex_init(&mtx, NULL);
            pthread_mutex_init(&mt[0], NULL);
            pthread_mutex_init(&mt[1], NULL);

            pthread_mutex_lock(&mt[1]); // first one starts
            for(j = 0; j < T; ++ j) {
                int *x = (int *)malloc(sizeof(int));
                *x = j;
                pthread_create(&t[j], NULL, doIt, (void *)x);
            }
            for(j = 0; j < T; ++ j)
                pthread_join(t[j], NULL);
            printf("Process %d has sum %d\n", getpid(), sum);

            int fd = open("c2p", O_WRONLY);
            struct package p;
            p.sum = sum;
            p.pid = getpid();

            pthread_mutex_lock(&mtx);
            write(fd, &p, sizeof(struct package));
            pthread_mutex_unlock(&mtx);

            close(fd);

            pthread_mutex_destroy(&mtx);
            pthread_mutex_destroy(&mt[0]);
            pthread_mutex_destroy(&mt[1]);
            exit(0);
        }

    int fd = open("c2p", O_RDONLY);
    for(i = 0; i < P; ++ i) {
        wait(0);
        struct package p;
        read(fd, &p, sizeof(struct package));
        printf("Received from pid: %d, sum: %d\n", (int)p.pid, p.sum);
    }
    close(fd);
    return 0;
}
