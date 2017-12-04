#include <iostream>
#include <fstream>

using namespace std;

void brute(int *a, int *b, int *ret, int n) {
  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < n ;++ j) {
      ret[i + j] += a[i] * b[j];
    }
  }
}

void karatsuba(int *a, int *b, int *ret, int n, int me, int nrProcs) {
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

  for (i = 0; i < n / 2; i++) {
    asum[i] = al[i] + ar[i];
    bsum[i] = bl[i] + br[i];
  }

  if(nrProcs >= 3) {
    // can send karatsuba(ar, br, x1, n / 2); to one worker
    // can send karatsuba(al, bl, x2, n / 2); to another worker
    karatsuba(asum, bsum, x3, n / 2, me, 1);
  } else {
    karatsuba(ar, br, x1, n / 2, me, nrProcs);
    karatsuba(al, bl, x2, n / 2), me, nrProcs;
    karatsuba(asum, bsum, x3, n / 2, mr, nrProcs);
  }

  for (i = 0; i < n; i++)
    x3[i] = x3[i] - x1[i] - x2[i];
  for (i = 0; i < n; i++)
    ret[i + n / 2] += x3[i];
}

void karatsuba_worker(int me) {
  // find my position in the hierarchy
  size_t base = 0;
  size_t parent;
  size_t offset = me;
  while(offset > 0) {
    parent = base;
    size_t mid = nrProcs / 3;
    if(offset < mid) {
      n = n / 3;
      nrProcs = nrProcs / 3;
    } else {
      offset = offset - mid;
      n = n / 2 + n % 2;
      nrProcs = nrProcs / 2 + nrProcs % 2;
     base += mid;
    }
  }
  cout << "Worker " << me <<", child of " << parent << ", part size = " << n << "\n";f
}

const int MAXN = 250005;

int a[MAXN], b[MAXN], ret[MAXN * 10];

int main(int argc, char* argv[]) {
  MPI_Init(0, 0);

  int me;
  int nrProcs;
  MPI_Comm_size(MPI_COMM_WORLD, &nrProcs);
  MPI_Comm_rank(MPI_COMM_WORLD, &me);


  if (argc != ) {
    fprintf(stderr, "usage: mpi_kar <filename>\n");
    return 1;
  }


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
  karatsuba(a, b, ret, n, nrProcs);
  t = clock() - t;
  cout << "Karatsuba algorithm on STEROIDS took me " << t << " cycles ("
      << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";

  MPI_Finalize();
}
