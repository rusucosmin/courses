#include <iostream>
#include <mpi.h>
#include <vector>
#include <time.h>
#include <stdint.h>
#include <time.h>
#include <stdio.h>

using namespace std;

const int MAXVALUE = 100;

void generate(vector<int>& v, size_t n) {
  v.resize(n);
  for(int i = 0; i < n; ++ i) {
    int x = rand() % MAXVALUE;
    v[i] = x;
  }
}

int main(int argc, char** argv) {
  srand(time(NULL));
  MPI_Init(0, 0);
  int me;
  int nrProcs;
  MPI_Comm_size(MPI_COMM_WORLD, &nrProcs);
  MPI_Comm_rank(MPI_COMM_WORLD, &me);

  unsigned n;
  vector<int> a, b;
  if (argc != 2 || 1 != sscanf(argv[1], "%u", &n)) {
    fprintf(stderr, "usage: mpi_naive <n>\n");
    return 1;
  }

  if (me == 0) {
    generate(a, n);
    generate(b, n);
    fprintf(stderr, "generated\n");
  }

  MPI_Finalize();
}
