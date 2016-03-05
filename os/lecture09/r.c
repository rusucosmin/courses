#include <stdio.h>

int main() {
    int a, b;

    a = 2;
    b = 7;

    b++;
    if(a > 3) {
        a++;
    }

    printf("a=%d b=%d\n", a, b);
    return 0;
}
