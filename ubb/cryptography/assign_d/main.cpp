#include <iostream>
#include <map>
#include <vector>
#include <fstream>
#include <math.h>

using namespace std;

inline void fact(int n) {
  n = max(n, -n);
  cerr << n << ": ";
  if(n == 1) {
    cerr << "1 ";
    return ;
  }
  vector <int> factors;
  for (int d = 2; d * d <= n; ++ d) {
    if(n % d == 0) {
      while(n % d == 0) {
        n /= d;
        cerr << d << ' ';
      }
    }
  }
  if (n > 1) {
    cerr << n;
  }
  cerr << '\n';
}

inline void solve(int n) {
  cerr << "------------solve(" << n << ")------------\n";
  map<int, int> b, a;
  map<int, double> x;
  b[-1] = 1;
  b[0] = a[0] = int(sqrt(n));
  cerr << a[0] << ' ' << sqrt(n) << '\n';
  x[0] = sqrt(n) - a[0];
  cerr << 0 << ' ' << x[0] << ' ' << a[0] << ' ' << b[0] << ' ' << b[0] * b[0] - n << '\n';
  vector <int> v;
  v.push_back(b[0] * b[0] - n);
  for(int i = 1; i < 20; ++ i) {
    a[i] = int(1.0 / x[i - 1]);
    x[i] = 1.0 / x[i - 1] - a[i];
    b[i] = (1LL * a[i] * b[i - 1] + b[i - 2]) % n;
    int aux = (b[i] * b[i]) % n;
    // n = 1000
    // -1 = 999 (mod 1000)
    // - n / 2 = n - n / 2


    // -i = n - i
    if(aux > n - aux) {
      aux = aux - n;
    }
    v.push_back(aux);
    cerr << i << ' ' << x[i] << ' ' << a[i] << ' ' << b[i] << ' ' << aux << '\n';
  }
  cerr << "Factorizing...\n";
  for(auto it : v) {
    fact(it);
  }
  cerr << '\n';
}

int main() {
  ifstream fin("input.in");
  ofstream fout("output.out");

  int n;
  fin >> n;
  //solve(9073);
  //solve(17873);
  solve(8027);
  solve(n);
}
