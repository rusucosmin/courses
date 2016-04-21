#include <stdio.h>
#include <math.h>

int main(int argc, char** argv) {
    int a, b, i, j;
    double r;

    if(argc < 3) {
        if(scanf("%d", &a) != 1) {
            fprintf(stderr, "Can't read first number\n");
            return 1;
        }
        if(scanf("%d", &b) != 1) {
            fprintf(stderr, "Can't read second number\n");
            return 1;
        }
    }
    else {
        if(sscanf(argv[1], "%d", &a) != 1) {
            fprintf(stderr, "Can't read first number\n");
            return 1;
        }
        if(sscanf(argv[2], "%d", &b) != 1) {
            fprintf(stderr, "Can't read second number\n");
            return 1;
        }
    }

    r = 0.0;
    for(i=0; i<a; i++) {
        for(j=0; j<b; j++) {
            r = sqrt(r+i+j);
        }
    }
    fprintf(stdout, "%lf\n", r);

    return 0;
}
