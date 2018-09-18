#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <strings.h>
#include <unistd.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void error(char *msg) {
    perror(msg);
    exit(0);
}

#define MAXT 100

struct tuple {
    int n;
    int port;
    int sock;
};

char thbuff[1024];
char thsnum[30];

void *compute_sum(void * args) {
    struct tuple * cur = (struct tuple *) args;
    struct sockaddr_in from;
    int fromlen = sizeof(struct sockaddr_in);
    int i;
    int sum = 0;
    for(i = 0; i < cur->n; ++ i) {
        int n = recvfrom(cur->sock, thbuff, 1024, 0, (struct sockaddr *) &from, &fromlen);
        if(n < 0)
            error("ERROR: reading vector");
        sum += atoi(thbuff);
    }
    sprintf(thsnum,"%d",sum);
    int n = sendto(cur->sock, thsnum, strlen(thsnum), 0, (struct sockaddr*)&from, fromlen);
    if(n < 0)
        error("ERROR: sending result(sum)");

    return NULL;
}

int starting_port = 2222;

int main(int argc, char *argv[]) {
    pthread_t thr[MAXT];
    struct tuple thr_args[MAXT];
    int t = 0;

    char buff[1024];
    char snum[30];

    int sock, length, fromlen, n, port = 2222;
    struct sockaddr_in server, th_server;
    struct sockaddr_in from;

    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if(sock < 0)
        error("ERROR: opening port\n");

    length = sizeof(server);
    bzero(&server, length);

    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(port);

    if(bind(sock, (struct sockaddr *) &server, length) < 0)
        error("ERROR: binding socket\n");

    printf("> LOG: server ready to accept connections\n");

    fromlen = sizeof(struct sockaddr_in);
    while(1) {
        n = recvfrom(sock, buff, 1024, 0, (struct sockaddr *) &from, &fromlen);
        if(n < 0)
            error("ERROR: receiving\n");
        write(1, "> LOG: received a datagram: ", 28);
        write(1, buff, n);
        write(1, "\n", 1);


        thr_args[t].n = atoi(buff);
        thr_args[t].port = ++ starting_port;
        thr_args[t].sock = socket(AF_INET, SOCK_DGRAM, 0);
        if(thr_args[t].sock < 0)
            error("ERROR: creating child socket\n");

        bzero(&th_server, length);

        th_server.sin_family = AF_INET;
        th_server.sin_addr.s_addr = INADDR_ANY;
        th_server.sin_port = htons(starting_port);

        if(bind(thr_args[t].sock, (struct sockaddr *) &th_server, length) < 0)
            error("ERROR: binding child socket\n");

        printf("> LOG: child new socket created\n");
        printf("> LOG: starting new thread on %d port", starting_port);
        pthread_create(&thr[t], NULL, compute_sum, (void *) &thr_args[t]);

        sprintf(snum,"%d",starting_port);

        n = sendto(sock, snum, strlen(snum), 0, (struct sockaddr*)&from, fromlen);

        if(n < 0)
            error("ERROR: sending data back\n");

        ++ t;
    }
    return 0;
}

