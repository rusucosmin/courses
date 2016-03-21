#include <stdio.h>

int main() {
    float a, b, c;
    scanf("%f%f%f", &a, &b, &c);
    printf("Numere introduse sunt: %f, %f si %f!\n", a, b, c);
    printf("Suma lor este: %f\n", a + b + c);
    printf("Media lor este: %f\n", (float)(a + b +c) / 3);
    return 0;
}
