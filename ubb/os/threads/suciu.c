/* 3. Write a C program that receives as arguments file names and processes them simultaneously using threads. The program transforms the files so that all words will begin with a capital letter. The modified files (containing the first letter words capitalized) will have the same name as the original files and will end with the number N (N is the thread id). You will create a thread for each file.
*/

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct thread {
    char *file;
    int id;
};

void* capitalize(void* arg) {
    struct thread aux = *(struct thread *)arg;
    char new[100], nr[100];
    strcpy(new, aux.file);
    sprintf(nr, "%d", aux.id);
    strcat(new, nr);
    FILE *f = fopen(aux.file, "r");
    FILE *g = fopen(new, "w");
    char c, last = ' ';
    while(fscanf(f, "%c", &c) == 1) {
        if((last < 'a' || last > 'z') && (last < 'A' || last > 'Z')) {
            c = toupper(c);
        }
        fprintf(g, "%c", c);
        last = c;
    }
    fclose(f);
    fclose(g);
    free(arg);
    return NULL;
}

int main(int argc, char *argv[]) {
    int i;
    pthread_t *t;
    t = (pthread_t*) malloc((argc - 1) * sizeof(pthread_t));
    for(i = 0 ; i < argc - 1 ; ++ i) {
        struct thread *arg = (struct thread *)malloc(sizeof(struct thread));
        arg->file = argv[i + 1];
        arg->id = i + 1;
        pthread_create(&t[i], NULL, capitalize, (void *)arg);
    }
    for(i = 0 ; i < argc - 1 ; ++ i) {
        pthread_join(t[i], NULL);
    }
    free(t);
    return 0;
}
