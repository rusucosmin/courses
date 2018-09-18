/*
7. Implementati un program C care are un tablou global de 10 int-uri numti "suma\_dupa\_rest". Programul va crea 7 threaduri, ficare dintre ele generand 100 de numere aleatoare. Fiecare numar va fi adunat la elemntul tabloului "suma\_dupa\_rest" corespunzator restului impartirii numarluliu la 10. Folositi mecanismele de sincronizare necesare pentru a asigura aclcularea corecta a sumelor.
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <time.h>

#define mod 10
#define T 7

pthread_t t[T];
pthread_mutex_t mtx[mod];

int sum_rest[mod];

void * doIt(void *arg) {
    int i;
    for(i = 0; i < 100; ++ i) {
        int x = rand() % 10000;
        printf("Thread mod: %d, nr: %d\n", x % 10, x);
        pthread_mutex_lock(&mtx[x % 10]);
        sum_rest[x % 10] += x;
        pthread_mutex_unlock(&mtx[x % 10]);
    }
    return NULL;
}

int main() {
    srand(time(NULL));
    int i;
    for(i = 0; i < mod; ++ i)
        pthread_mutex_init(&mtx[i], NULL);
    for(i = 0; i < T; ++ i)
        pthread_create(&t[i], NULL, doIt, NULL);
    for(i = 0; i < T; ++ i)
        pthread_join(t[i], NULL);
    for(i = 0; i < mod; ++ i)
        pthread_mutex_destroy(&mtx[i]);
    printf("Father:\n");
    for(i = 0; i < mod; ++ i)
        printf("%d ", sum_rest[i]);
    printf("\n");
    return 0;
}
