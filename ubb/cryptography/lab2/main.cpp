#include <iostream>
#include <fstream>
#include "bigint.h"

const int T = 1;

inline bigint gcd_subtract(bigint x, bigint y) {
  if (x.isZero()) {
    return y;
  }
  if (y.isZero()) {
    return x;
  }
  while (x != y) {
    if (x > y) {
      x = x - y;
    }
    else {
      y = y - x;
    }
  }
  return x;
}

inline bigint gcd_division(bigint x, bigint y) {
  if (x.isZero()) {
    return y;
  }
  if (y.isZero()) {
    return x;
  }
  //gcd(a, b) = gcd(b, a % b)
  bigint r;
  while (x % y != 0) {
    r = x % y;
    x = y;
    y = r;
  }
  return y;
}

inline bool isPrime(bigint &x) {
  if (x == 1L) {
    return false;
  }
  if (x == 2L) {
    return true;
  }
  // x = d1 * d2
  // d1 <= d2
  // d1 <= sqrt(d1)
  for(bigint d = 2; d * d <= x; d += 1) {
    if (x % d == 0) {
      return false;
    }
  }
  return true;
}

inline bigint gcd_factorization(bigint x, bigint y) {
  bigint prime(2);
  bigint _gcd(1);
  while (prime * prime <= x && prime * prime <= y) {
    while (x % prime == 0 && y % prime == 0) {
      x /= prime;
      y /= prime;
      _gcd *= prime;
    }
    prime += 1;
    while(!isPrime(prime)) {
      prime += 1;
    }
  }
  return _gcd;
}

int main() {
  ofstream _log("stats_.txt");
  for(int i = 0; i < T; ++ i) {
    cerr << "starting test " << i << '\n';
    auto start = std::chrono::high_resolution_clock::now();
    ifstream fin(to_string(i) + ".in");
    ofstream fout(to_string(i) + ".out");
    int dcount;
    bigint x, y;
    fin >> dcount >> x >> y;
    _log << dcount << ' ';
    bigint _gcd = gcd_division(x, y);
    //bigint _gcd = gcd_subtract(x, y);
    //bigint _gcd = gcd_factorization(x, y);
    cerr << "gcd division = " << _gcd << '\n';
    //cerr << "gcd subtraction = " << gcd_subtract(x, y) << '\n';
    //cerr << "gcd factorization = " << gcd_factorization(x, y) << '\n';
    auto finish = std::chrono::high_resolution_clock::now();
    auto total =  std::chrono::duration_cast<std::chrono::microseconds>(finish - start);
    _log << total.count() << "\n";
    fout << _gcd << '\n';
  }
}
