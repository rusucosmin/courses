#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>


char filename[100], buffer[1000];

int main() {
    int pipefd[2];
    scanf("%s", filename);
    freopen(filename, "r", stdin);
    fread(buffer, 1, 1000, stdin);
    pipe(pipefd);
    if(fork() == 0) { /*child reads from parent*/
        close(pipefd[1]);

        char buff;
        printf("Copilil scrie asta");
        while(read(pipefd[0], &buff, 1) > 0)
            write(STDOUT_FILENO, &buff, 1);
        printf("Fiul a citit!");

        write(STDOUT_FILENO, "\n", 1);
        close(pipefd[0]);
    }
    else {
        close(pipefd[0]); /*parent doesn't read*/
        write(pipefd[1], buffer, strlen(buffer));
        close(pipefd[1]);
        printf("Parintele a terminat de scris");
        wait(NULL); /*wait for child*/
        exit(EXIT_SUCCESS);
    }
    return 0;
}
