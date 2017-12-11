#include <iostream>
#include <fstream>
#include <assert.h>

using namespace std;

void brute(int *a, int *b, int *ret, int n) {
  for(int i = 0; i < 2 * n; ++ i) {
    ret[i] = 0;
  }
  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < n; ++ j) {
      ret[i + j] += a[i] * b[j];
    }
  }
}

void karatsuba(int *a, int *b, int *ret, int n)
{
  if (n <= 4) {
    brute(a, b, ret, n);
    return;
  }

  int i;
  int *ar = &a[0];                 // low-order half of a
  int *al = &a[n / 2];             // high-order half of a
  int *br = &b[0];                 // low-order half of b
  int *bl = &b[n / 2];             // high-order half of b
  int *asum = &ret[n * 5];         // sum of a's halves
  int *bsum = &ret[n * 5 + n / 2]; // sum of b's halves
  int *x1 = &ret[n * 0];           // ar*br's location
  int *x2 = &ret[n * 1];           // al*bl's location
  int *x3 = &ret[n * 2];           // asum*bsum's location

  for (i = 0; i < n / 2; i++)
  {
    asum[i] = al[i] + ar[i];
    bsum[i] = bl[i] + br[i];
  }

  karatsuba(ar, br, x1, n / 2);
  karatsuba(al, bl, x2, n / 2);
  karatsuba(asum, bsum, x3, n / 2);

  for (i = 0; i < n; i++)
    x3[i] = x3[i] - x1[i] - x2[i];
  for (i = 0; i < n; i++)
    ret[i + n / 2] += x3[i];
}

const int MAXN = 250005;
int a[MAXN], b[MAXN], ret[10 * MAXN], check[3 * MAXN];

inline void verify(int *a, int *b, int *res, int n) {
  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < n; ++ j) {
      check[i + j] += a[i] * b[j];
    }
  }
  for(int i = 0; i < 2 * n - 1; ++ i) {
    assert(res[i] == check[i]);
  }
}

int main(int argc, char* argv[]) {
  clock_t t;
  t = clock();
  ifstream fin(argv[1]);
  int n;
  fin >> n;
  for(int i = 0; i < n; ++ i) {
    fin >> a[i];
  }
  for(int i = 0; i < n; ++ i) {
    fin >> b[i];
  }
  while(n & (n - 1)) {
    ++ n;
  }
  karatsuba(a, b, ret, n);
  verify(a, b, ret, n);
  t = clock() - t;
  cout << "Karatsuba algorithm on STEROIDS took me " << t << " cycles ("
      << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";

}
