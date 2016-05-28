#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <pthread.h>
#include <time.h>


/*
 *
 * 2. Sa se scrie un program care creeaza 7 thread-uri si are un tablou global de 10 int-uri numit SUM, care face sumele numerelor in functie de restul
 *
 *  impartitii la 10.   Fiecare thread va genera numere aleatoare intre 0 si 100, si, in functie de numarul obtinut, il aduna la itemul din tablou
 *
 *   corespunzator restului impartiii la 10. Thread-urile se opresc cand   s-au generat exact 5 numere cu ultima cifra 5 . Programul principal afiseaza 
 *
 *    sumele adunate (atat suma cat si numerele care au participat la ea) in tabloul global si apoi se termina. Folositi mecanismele de sincronizare necesare
 *
 *     pentru a asigura calcularea corecta si eficienta a sumelor.
 * */

#define T 7
#define mod 10

pthread_t t[T];
pthread_mutex_t mtx[mod], m;
int sum[mod];
int val[mod][1000];
int cnt;

void * doIt(void *arg) {
    while(cnt < 5) {
        pthread_mutex_lock(&m);
        if(cnt >= 5) {
            pthread_mutex_unlock(&m);
            break;
        }   
        pthread_mutex_unlock(&m);
        int x = rand() % 101;
        int r = x % 10;
        printf("%d ", x);   
        pthread_mutex_lock(&mtx[r]);
        sum[r] += x;
        val[r][ ++ val[r][0] ] = x;
        if(x % 10 == 5)
            ++ cnt;
        pthread_mutex_unlock(&mtx[r]);
    }
    return NULL;
}


int main() {
        srand(time(NULL));
    int i, j;
    pthread_mutex_init(&m, NULL);
    printf("Nr ");
    for(i = 0; i < mod ; ++ i)
        pthread_mutex_init(&mtx[i], NULL);
    for(i = 0; i < T;  ++ i)
        pthread_create(&t[i], NULL, doIt, NULL);
    for(i = 0; i < T; ++ i)
        pthread_join(t[i], NULL);
    printf("\n");
    for(i = 0 ; i < mod ; ++ i)
        pthread_mutex_destroy(&mtx[i]);
    pthread_mutex_destroy(&m);
    printf("Numere cu ultima cifra 5: %d\n", cnt);
    for(i = 0; i < mod; ++ i) {
        printf("sum[%d] = ", i);
        for(j = 1; j <= val[i][0]; ++ j) {
            if(j != 1)
                printf("+ ");
            printf("%d ", val[i][j]);
        }
        printf("= %d\n", sum[i]);
    }
    pthread_mutex_destroy(&m);
    return 0;
}

