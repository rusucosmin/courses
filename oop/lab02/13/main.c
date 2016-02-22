/***
Author: Cosmin Rusu
13.
a. Determine the first 10 natural numbers (x1, x2, …, x10) greater than 2 with the following
property: all the natural numbers smaller than xi and that are relatively prime with xi, are prime,
i =1,2, …, n.
b. Given a vector of numbers, find the longest contiguous subsequence such that any consecutive
elements contain the same digits.
*/

#include <stdio.h>
#include <stdlib.h>

#define maxn 10005
#define maxvalue 1000005

typedef struct {
    int arr[maxn];
    int length;
} vector;

char sieve[maxvalue];

void printConsole(char *op) {
/**
    Function to read the type of operation:
    Input: Nothing
    Output: op which can be either 'a' or 'b' (for our problem)
*/
    printf("Task 13!\nPlease input 'a' or 'b'!\n");
    scanf("%c", op);
    while(*op != 'a' && *op != 'b') {
        printf("Not valid!\nPlease input 'a' or 'b'!");
        scanf("%c", op);
    }
}

vector readArray() {
/**
    Function to read a vector from the user.
    Input: Nothing
    Output: the vector which was read
*/
    vector v;
    int i;
    printf("n = ");
    scanf("%d", &v.length);
    for(i = 0 ; i < v.length ; ++ i) {
        scanf("%d", v.arr + i);
    }
    return v;
}

void printArray(vector v) {
/**
    Function to print a vector to the standard output.
    Input: v: vector
    Output: the content of the vector v on stdout
*/
    int i;
    for(i = 0 ; i < v.length ; ++ i)
        printf("%d ", v.arr[i]);
    printf("\n");
}

int sameDigits(int a, int b) {
/**
    Function to check if two natural number have the same digits in it's representation in base 10.
    Input: a, b: natural numbers
    Output: 1 if they share the same number of digits
            0 otherwise
*/
    int fr1[10], fr2[10], i;
    memset(fr1, 0, sizeof(fr1));
    memset(fr2, 0, sizeof(fr2));
    while(a) {
        ++ fr1[a % 10];
        a /= 10;
    }
    while(b) {
        ++ fr2[b % 10];
        b /= 10;
    }
    for(i = 0 ; i < 10 ; ++ i)
        if((fr1[i] == 0 && fr2[i] != 0) || (fr1[i] != 0 && fr2[i] == 0))
            return 0;
    return 1;
}

vector solveB(vector v) {
/**
    Function to solve the second task
    Input: v: vector
    Output: the longest subsequence satisfying the statement condition (prints to the standard ouput)
    Time Complexity for the algorithm O(N)
    Space complexity: O(1) extra space (without counting the array)
*/
    int i = 0, maxi = 1, limax = 0;
    while(i < v.length) {
        int ls = i;
        while(ls + 1 < v.length && sameDigits(v.arr[ls], v.arr[ls + 1]) == 1)
            ++ ls;
        if(maxi < ls - i + 1) {
            maxi = ls - i + 1;
            limax = i;
        }
        i = ls + 1;
    }
    vector ret;
    ret.length = 0;
    for(i = limax ; i < limax + maxi ; ++ i) {
        ret.arr[ret.length ++ ] = v.arr[i];
    }
    return ret;
}

void sieveBuild() {
/**
    Function to preprocess the Sieve of Erathostenes
    Builds the vector sieve with the following property:
        sieve[i] = 0 implies that i is prime
        sieve[i] = 1 implies that i is not prime
*/
    sieve[0] = sieve[1] = 1; /// they are not prime
    int i, j;
    for(i = 2 ; (long long)i < maxvalue ; ++ i)
        if(sieve[i] == 0)
            for(j = i + i ; j < maxvalue ; j += i)
                sieve[j] = 1;
}

int prime(int n) {
/**
    Function to check if a natural number is prime.
    We use the sieve of Erathostenes to check that.
    Input: n
    Output: 1 if the number is prime
            0 if the number is not prime
*/
    if(sieve[n] == 1)
        return 0;
    return 1;
}

int gcd(int x, int y) {
/**
    Functiont o return the gratesc common divisor of two natural numbers x and y.
    Input: x, y: natural numebr
    Output: the greatest common divisor of x and y;
*/
    if(y == 0)
        return x;
    return gcd(y, x % y);
}

int special(int n) {
/**
    Function to check if a number is special or not. And by special we mean the
    property given in the statement.
    Input: integer numer n
    Output: 1 if the number is special
            0 if not
*/
    int div;
    for(div = 2 ; div < n ;++ div) {
        if(gcd(n, div) == 1 && prime(div) == 0)
            return 0;
    }
    return 1;
}

vector solveA() {
/**
    Function to solve the second task.
    Idea: keep searching for such 'special' numbers until we have found more than ten

    Note: if I'm not mistaking, there are only 9 numbers which satisfys the condition
    the 10th number may exist, but can be extremly large...
*/
    int cnt = 0, n = 2;
    vector v;
    v.length = 0;
    for(cnt = 0 ; cnt < 9 ; ++ cnt) {
        while(special(n) == 0)
            ++ n;
        v.arr[v.length ++] = n;
        ++ n;
    }
    return v;
}

int main()
{
    printf("%d\n", special(3));
    char op;
    printConsole(&op);
    if(op == 'a') {
        sieveBuild();
        vector answer;
        answer = solveA();
        printf("Task (a):\n");
        printArray(answer);
    }
    else {
        printf("Task (b):\n");
        vector v;
        v = readArray();
        vector ans;
        ans = solveB(v);
        printArray(ans);
    }
    return 0;
}
