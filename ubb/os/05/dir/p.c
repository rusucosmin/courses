#include <stdio.h>
#include <math.h>

int main(int argc, char** argv) {
    int a, b, i, j;
    double r;

    if(argc < 3) {
        scanf("%d", &a);
        scanf("%d", &b);
//        return 1; // de ce 1?
    }
    else {
        sscanf(argv[1], "%d", &a);
        sscanf(argv[2], "%d", &b);
    }

    r = 0.0;
    for(i=0; i<a; i++) {
        for(j=0; j<b; j++) {
            r = sqrt(r + i + j);
        }
    }
    printf("%lf\n", r);

    return 0;
}
