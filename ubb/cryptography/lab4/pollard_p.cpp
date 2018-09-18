#include <iostream>
#include <fstream>
#include <functional>
#include <vector>
#include <algorithm>
#include <assert.h>

using namespace std;

inline long long gcd(long long a, long long b) {
  if(!b) return a;
  return gcd(b, a % b);
}

inline long long mod(long long a) {
  return max(a, -a);
}

long long solve(long long n, function<long long(long long)>f) {
   /* x ← 2; y ← 2; d ← 1
    while d = 1:
        x ← g(x)
        y ← g(g(y))
        d ← gcd(|x - y|, n)
    if d = n:
        return failure
    else:
        return d
        */
  long long x = 2;
  long long y = 2;
  long long d = 1;
  for(int i = 0; d == 1 ; ++ i) {
    x = f(x);
    y = f(f(y));
    d = gcd(mod(x - y), n);
  }
  if(d == n) {
    cerr << "Error, it's not working!\n";
    return -1;
  } else {
    return d;
  }
}

inline void runTests() {
  const int T = 100;
  srand(time(NULL));
  for(int i = 0; i < T; ++ i) {
    cerr << "Running test #" << i + 1 << "\n";
    long long x = 1LL * rand() * rand();
    cerr << "Factorizing " << x << '\n';
    long long p = solve(x, [](long long x)->long long{return x*x+x+1;});
    assert(p == -1 || x % p == 0);
  }
  cout << "All tests have passed!\n";
}


int main(int argv, char *args[]) {
//  runTests();
  clock_t t;
  t = clock();

  long long  n = 4087;
  string filename = "input.in";
  if(argv > 1) {
    filename = args[1];
  }
  ifstream fin(filename);
  fin >> n;
  ofstream fout("pollard_p.out");
  fout << n << '\n';
  long long prime = solve(n, [](long long x)->long long{return x*x+2*x+1;});
  assert(n % prime == 0);
  fout << prime << ' ' << n / prime << '\n';

  t = clock() - t;
  cout << " | `" << n << "` | POLLARD RHO  | `" << t << "` | `"
    << static_cast<float> (t) / CLOCKS_PER_SEC * 1000 << "` |\n";
  return 0;
}
