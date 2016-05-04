/*
2. Calculate the sum of the elements in a bidimensional matrix, using a separate thread to calculate the sum
of each row. The main thread adds up these sums printing the final result.
*/

#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

int *sum, **a, n, m;
pthread_t* t;

void* doIt(void *arg) {
    int id = *(int *)arg, i;
    int line = 0;
    for(i = 0; i < m; ++ i) {
        sum[id] += a[id][i];
        line += a[id][i];
    }
    free(arg);
    return (void *)line;
}

int main() {
    int i, j;
    scanf("%d%d", &n, &m);
    a = (int**)malloc(n * sizeof(int*));
    sum = (int *)malloc(n * sizeof(int));
    for(i = 0; i < n; ++ i) {
        sum[i] = 0;
        a[i] = (int*) malloc(m * sizeof(int));
        for(j = 0; j < m; ++ j) {
            scanf("%d", &a[i][j]);
        }
    }

    t = (pthread_t*) malloc(n * sizeof(pthread_t));
    for(i = 0; i < n; ++ i) {
        int* x = (int *) malloc(sizeof(int));
        *x = i;
        pthread_create(&t[i], NULL, doIt, (void*)x);
    }
    int total = 0;
    int total2 = 0;
    for(i = 0; i < n; ++ i) {
        void *aux;                  /// You can also return the sum of a line on the doIt() function
        pthread_join(t[i], &aux);
        total2 += (int)aux;
        printf("Thread %d computed %d\n", i, sum[i]);
        total += sum[i];
        free(a[i]);
    }
    printf("The total sum is %d\n", total);
    free(a);
    free(t);
    free(sum);
    return 0;
}
