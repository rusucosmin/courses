#include <stdio.h>

void g() {
    int x[3] = {2, 22, 222};
    printf("G says: %d %d %d\n", x[0], x[1], x[2]);
}

int* f() {
    int x[3] = {1, 11, 111};
    printf("F says: %d %d %d\n", x[0], x[1], x[2]);
    return x; // NOOOOOOOOOO
}

int main() {
    int* a = f();
    g();
    printf("MAIN says: %d %d %d\n", a[0], a[1], a[2]);
    return 0;
}
