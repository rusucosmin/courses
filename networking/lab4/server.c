#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <strings.h>

void error(char *msg) {
    perror(msg);
    exit(0);
}

int starting_port = 2222;

int main(int argc, char *argv[]) {
    int sock = 2222, length, fromlen, n;
    struct sockaddr_in server;
    struct sockaddr_in from;
    char buff[1024];

    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if(sock < 0)
        error("ERROR: Opening port\n");

    length = sizeof(server);
    bzero(&server, length);

    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(sock);

    if(bind(sock, (struct sockaddr *) &server, length) < 0)
        error("ERROR: Binding socket\n");

    fromlen = sizeof(struct sockaddr_in);
    while(1) {
        n = recvfrom(sock, buff, 1024, 0, (struct sockaddr *) &from, &fromlen);
        if(n < 0)
            error("ERROR: receiving\n");
        write(1, "Received a datagram: ", 21);
        write(1, buff, n);
        n = sendto(sock, "Got your message\n", 17, 0, (struct sockaddr*)&from, fromlen);
        if(n < 0)
            error("ERROR: sending data back\n");
    }
    return 0;
}

