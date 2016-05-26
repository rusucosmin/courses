/*j
3. Se creeaza un subproces. Se creeaza 2 thread-uri in subproces. Threadurile citesc cate un numar (alternativ) si il aduna la o suma. Se repeta cat timp suma < 100. Din subproces, se transmite printr-un pipe rezultatul la procesul principat. Procesul principal afiseaza rezultatul.
*/
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

pthread_mutex_t m[2];
pthread_t t[2];
int sum;

void* doIt(void *arg) {
    int id = *(int *)arg, n;
    while(sum < 100) {
        pthread_mutex_lock(&m[id]);
        if(sum < 100) {
            printf("Thread %d\nn = ", id);
            scanf("%d", &n);
            sum += n;
        }
        pthread_mutex_unlock(&m[1 - id]);
    }
    free(arg);
    return NULL;
}

int main() {
    int c2p[2], i;
    pipe(c2p);
    /// 0 - read
    /// 1 - write
    if(fork()) {
        close(c2p[0]);

        for(i = 0; i < 2; ++ i)
            pthread_mutex_init(&m[i], NULL);

        pthread_mutex_lock(&m[1]); /// 0 starts
        for(i = 0; i < 2; ++ i) {
            int * x = (int *)malloc(sizeof(int));
            *x = i;
            pthread_create(&t[i], NULL, doIt, x);
        }
        for(i = 0; i < 2 ; ++ i)
            pthread_join(t[i], NULL);

        write(c2p[1], &sum, sizeof(int));
        close(c2p[1]);

        for(i = 0; i < 2; ++ i)
            pthread_mutex_destroy(&m[i]);
        exit(0);
    }
    close(c2p[1]);
    int aux;
    read(c2p[0], &aux, sizeof(int));
    printf("Tata lor: %d\n", aux);
    wait(0);
    return 0;
}
