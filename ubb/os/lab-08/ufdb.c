#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    int su[2], uw[2];

    pipe(su);
    pipe(uw);

    // sort a.txt
    if(fork() == 0) {
        close(su[0]); close(uw[0]); close(uw[1]);
        dup2(su[1], 1);
        execl("/usr/bin/sort", "/usr/bin/sort", "a.txt", NULL);
        exit(0);
    }

    // uniq
    if(fork() == 0) {
        close(su[1]); close(uw[0]);
        dup2(su[0], 0);
        dup2(uw[1], 1);
        execl("/usr/bin/uniq", "/usr/bin/uniq", NULL);
        exit(0);
    }

    // wc -l
    if(fork() == 0) {
        close(su[0]); close(su[1]); close(uw[1]);
        dup2(uw[0], 0);
        execl("/usr/bin/wc", "/usr/bin/wc", "-l", NULL);
        exit(0);
    }

    close(su[0]); close(su[1]); close(uw[0]); close(uw[1]); // try moving this line after the waits and see it work wrongly.
    wait(0); wait(0); wait(0);

    return 0;
}
