#include <stdio.h>

int main() {
    float x, f_x;
    scanf("%f", &x);
    if(x < 1)
        f_x = 3 * x * x + 1;
    else
        f_x = x - 1;
    printf("f(%f) = %f\n", x, f_x);
    return 0;
}
