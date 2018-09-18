/*
2. *Grebla(?)* Implement two processes in C that communicate through PIPE. Process A sends a string to process B, B eliminates maximum 3 vowels from it and sends it back to A, which eliminates also maximum 3 vowels, and sends it back to B and so on. The processes stop when they either receive or send a string that does not contain vowels.
    - **FIlE: `vowel.c`**
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>

struct pachet {
    char s[1000];
};

int count_vowels(char *s) {
    int cnt = 0, i;
    for(i = 0; i < strlen(s); ++ i)
        if(strchr("aeiou", s[i]))
            ++ cnt;
    return cnt;
}

void take_away_vowels(char *s) {
    int cnt = 0, i;
    for(i = 0; i < strlen(s) && cnt < 3; ++ i)
        if(strchr("aeiou", s[i])) {
            strcpy(s + i, s + i + 1);
            -- i;
            ++ cnt;
        }
}

int main() {
    int c2p[2];
    int p2c[2];
    /// 0 - read
    /// 1 - write
    pipe(c2p);
    pipe(p2c);
    struct pachet p;
    if(fork() == 0) {
        close(p2c[1]);
        close(c2p[0]);

        do {
        read(p2c[0], &p, sizeof(struct pachet));
        take_away_vowels(p.s);
        printf("B: %s\n", p.s);
        write(c2p[1], &p, sizeof(struct pachet));
        } while(count_vowels(p.s) > 0);

        close(p2c[0]);
        close(c2p[1]);
        exit(0);
    }
    scanf("%s", p.s);
    close(p2c[0]);
    close(c2p[1]);
    while(count_vowels(p.s) > 0) {
        printf("A: %s\n", p.s);
        write(p2c[1], &p, sizeof(struct pachet));
        read(c2p[0], &p, sizeof(struct pachet));
        take_away_vowels(p.s);
    }
    close(p2c[1]);
    close(c2p[0]);
    wait(0);
    return 0;
}
