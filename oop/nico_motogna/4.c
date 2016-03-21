#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    int r;
    while(b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    printf("%d\n", a);
    return 0;
}
