#include <stdio.h>

int fact(int n) {
    int fact = 1, i;
    for(i = 1 ; i <= n;  ++ i) {
        fact = fact * i;
    }
    return fact;
}

int main() {
    printf("fact(%d) = %d\n", 5, fact(5));
    return 0;
}
