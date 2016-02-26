#include <stdio.h>
#include <malloc.h>

int main() {
    int n;
    printf("n = ");
    scanf("%d", &n);
    int *arr, i, s = 0;
    arr = (int *) malloc(n * sizeof(int));
    for(i = 0 ; i < n ; ++ i)
        scanf("%d", &arr[i]);
    for(i = 0 ; i < n ; ++ i)
        s = s  + arr[i];
    printf("s = %d\navg = %2f\n", s, (double) s / n);
    return 0;
}
