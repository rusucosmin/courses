#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <fcntl.h>

int main() {
    int a2b, b2a, n;

    mkfifo("./a2b", 0600);
    mkfifo("./b2a", 0600);

    n = 5;

    a2b = open("./a2b", O_WRONLY);
    b2a = open("./b2a", O_RDONLY);

    write(a2b, &n, sizeof(int));
    read(b2a, &n, sizeof(int));
    printf("%d\n", n);

    close(a2b);
    close(b2a);

    unlink("./a2b");
    unlink("./b2a");
    return 0;
}
