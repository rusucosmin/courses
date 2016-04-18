/*

Sa se scrie un program care citeste un numar de la tastatura,
creeaza un proces fiu, trimite fiului numarul citit, fiul genereaza
atatea numere aleatorii cat este valoarea numerica primita
de la parinte si trimite aceste numere aleatorii parintelui
care le afiseaza.

*/

#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    srand(time(NULL));
    int p2c[2], c2p[2], n;
    pipe(p2c);
    pipe(c2p);
    int res = fork();
    if(res < 0) {
        printf("Error while fork-ing\n");
        return 0;
    }
    /// [0] - read
    /// [1] - write
    if(res == 0) {
        close(p2c[1]);                      /// close write parent -> child
        close(c2p[0]);                      /// close read child -> parent
        read(p2c[0], &n, sizeof(int));
        close(p2c[0]);                      /// close read parent -> child
        for(int i = 1 ; i <= n ; ++ i) {
            int x = rand();
            printf("Son: %d\n", x);
            write(c2p[1], &x, sizeof(int));
        }
        close(c2p[1]);                      /// close write child -> parent
        exit(0);
    }
    scanf("%d", &n);
    close(p2c[0]);                          /// close read parent -> child
    close(c2p[1]);                          /// close write child -> parent
    write(p2c[1], &n, sizeof(int));
    close(p2c[1]);                          /// close write parent -> child
    for(int i = 1 ; i <= n ; ++ i) {
        int x;
        read(c2p[0], &x, sizeof(int));
        printf("Father: %d\n", x);
    }
    close(c2p[0]);                          /// close read child -> parent
    wait(0);                                /// wait for the child to die, pls
    return 0;
}
