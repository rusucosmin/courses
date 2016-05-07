/*
4. Implement a program that gets as arguments a file name followed by words. For each word, create a separate
thread that counts its appearances in the given file.  Print out the sum of the appearances of all words.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <string.h>

char *filename;

/// "cat README.md|grep -o html|wc -l"
void* count(void *arg) {
    char *word = (char *)arg;
    char *cmd = (char *) malloc((30 + strlen(filename) + strlen(word))*sizeof(char));
    strcpy(cmd, "cat ");
    strcat(cmd, filename);
    strcat(cmd, "|grep -o ");
    /**
        strcat(cmd, "|grep -o '\\<"); 
        TODO We can use this command to count only full words containing word. With the uncommented version, we count the word 'int' in printf().
    */
    strcat(cmd, word);
    strcat(cmd, "|wc -l");
    /**
        strcat(cmd, "\\>'|wc -l");
        See above(line 22)!
    */
    FILE *f = popen(cmd, "r");
    int *cnt = (int*) malloc(sizeof(int));
    fscanf(f, "%d", cnt);
    printf("Thread found in '%s' the word '%s' %d number of times\n", filename, word, *cnt);
    free(cmd);
    fclose(f);
    return (void *)cnt;
}

int main(int argc, char ** argv) {
    if(argc < 3) {
        printf("Not enough parameters!\n");
        return 1;
    }
    filename = argv[1];
    int T = argc - 2, i;
    pthread_t *t = (pthread_t*) malloc(T * sizeof(pthread_t));
    for(i = 0 ; i < T ; ++ i) {
        pthread_create(&t[i], NULL, count, (void*) argv[i + 2]);
    }
    int sum = 0;
    for(i = 0 ; i < T ; ++ i) {
        void *ret;
        pthread_join(t[i], &ret);
        sum += *(int *)ret;
        free(ret);
    }
    free(t);
    printf("Sum of appearances: %d.\n", sum);
    return 0;
}
