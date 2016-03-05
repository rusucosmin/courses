#include <stdio.h>
#include <signal.h>

void handler(int sgn) {
    printf("NO!\n");
    signal(SIGINT, handler);
}

int main() {
    signal(SIGINT, handler);
    while(1);
    return 0;
}
