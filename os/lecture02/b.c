#include <stdio.h>
#include <string.h>

int main() {
    char w[100];

    while(1) {
        scanf("%s", w);
        if(strcmp(w, "done") == 0) {
            break;
        }
    }
    printf(":-)\n");

    return 0;
}
