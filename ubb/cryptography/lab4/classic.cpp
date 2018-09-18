#include <iostream>
#include <fstream>
#include <vector>
#include <time.h>
#include <stdio.h>
#include <assert.h>

using namespace std;

inline vector<pair<long long, int>> factorize(long long n) {
  vector <pair<long long, int>> v;
  long long p = 2;
  while(p * p <= n) {
    if(n % p == 0) {
      long long cnt = 0;
      while(n % p == 0) {
        cnt ++;
        n /= p;
      }
      v.push_back(make_pair(p, cnt));
    }
    ++ p;
  }
  if(n != 1) {
    v.push_back(make_pair(n, 1));
  }
  return v;
}

inline long long pow(long long a, int n) {
  long long p = 1;
  for(; n ; n >>= 1) {
    if(n & 1) {
      p = p * a;
    }
    a = a * a;
  }
  return p;
}

inline void runTests() {
  const int T = 100;
  srand(time(NULL));
  for(int i = 0; i < T; ++ i) {
    cerr << "Running test #" << i + 1 << "\n";
    long long x = 1LL * rand() * rand();
    cerr << "Factorizing " << x << '\n';
    long long p = 1;
    for(auto it : factorize(x)) {
      p *= pow(it.first, it.second);
    }
    assert(p == x);
  }
  cout << "All tests have passed!\n";
}


int main(int argv, char * args[]) {
//  runTests();
  clock_t t;
  t = clock();

  string filename = "input.in";

  if(argv > 1) {
    filename = args[1];
  }

  ifstream fin(filename);
  long long n;

  fin >> n;

  ofstream fout("classic.out");
  fout << n << '\n';
  for(auto it : factorize(n)) {
    fout << it.first << ' ' << it.second << '\n';
  }

  t = clock() - t;
  cout << " | `" << n << "` | CLASSIC ALGORITHM  | `" << t << "` | `"
    << static_cast<float> (t) / CLOCKS_PER_SEC * 1000 << "` |\n";
  return 0;
}
