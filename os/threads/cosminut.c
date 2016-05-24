#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include <unistd.h>
#include <time.h>

int one=0,two=0,more=0;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;

void* f( void *p)
{
    while(one<5 || two<5 || more<5)
    {
        int n = 1 + rand()%999;
        printf("Valoare: %d \n",n);
        if(n/10==0)
        {
            pthread_mutex_lock(&m);
            one++;
            pthread_mutex_unlock(&m);
        }
        else if(n/100==0)
        {
            pthread_mutex_lock(&m);
            two++;
            pthread_mutex_unlock(&m);
        }
        else
        {
            pthread_mutex_lock(&m);
            more++;
            pthread_mutex_unlock(&m);
        }
    }
    return NULL;
}

int main()
{
    srand(time(NULL));
    pthread_mutex_init(&m, NULL);
    pthread_t T[7];
    int i;
    for(i=0;i<=6;i++)
        pthread_create(&T[i],NULL,f,NULL);
    for(i=0;i<7;i++)
        pthread_join(T[i],NULL);
    printf("One digit: %d, two digits: %d, more: %d \n",one,two,more);
    pthread_mutex_destroy(&m);
    return 0;
}
