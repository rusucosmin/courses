#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>

using namespace std;

struct sys {
  long long a, mod;
  sys(long long a, long long mod): a(a), mod(mod) {}
};

inline long long extendedGCD(long long a, long long b, long long &x, long long &y) {
  if(!b) {
    x = 1;
    y = 0;
    return a;
  }
  long long x0, y0;
  long long gcd = extendedGCD(b, a % b, x0, y0);
  x = y0;
  y = x0 - (a / b) * y0;
  return gcd;
}

inline long long GCD(long long a, long long b) {
  if(!b) {
    return a;
  }
  return GCD(b, a % b);
}

inline long long invmod(long long a, long long mod) {
  long long x = 0, y = 0;
  long long gcd = extendedGCD(mod, a, x, y);
  // now x and y is the solution of the equation x * mod + a * y = gcd => y / gcd is the invmod of a
  return y / gcd;
}

inline bool check(int x, unordered_map<int, bool> &cnt) {
  int d = 2;
  do {
    if (x % d == 0) {
      if (cnt[d]) {
        return true;
      }
      if (cnt[x / d]) {
        return true;
      }
      cnt[d] = cnt[x / d] = 1;
      while (x % d == 0) {
        x /= d;
      }
    }
    ++ d;
  } while(d * d <= x);
  return false;
}

inline bool incompatible(vector <sys> v) {
  for(int i = 0; i < v.size(); ++ i) {
    for(int j = 0; j < v.size(); ++ j) {
      long long _gcd = GCD(v[i].mod, v[j].mod);
      if (v[i].a % _gcd != v[j].a % _gcd) {
        return true;
      }
    }
  }
  return false;
}

inline long long solve(vector <sys> v) {
  if(incompatible(v)) {
    return -1;
  }
  long long P = 1;
  for(auto it : v) {
    P *= it.mod;
  }
  unordered_map<int, bool> cnt;
  long long sol = 0;
  for(auto it : v) {
    if(check(it.mod, cnt)) {
      return -1;
    }
    long long M = P / it.mod;
    sol += ((it.a * M * invmod(M, it.mod)) % P);
    sol %= P;
  }
  return (sol + P) % P;
}

inline void solve(string filename) {
  ifstream fin(filename);
  int n;
  vector <sys> eq;
  fin >> n;
  while(n --) {
    long long a, n;
    fin >> a >> n;
    eq.push_back(sys(a, n));
  }
  cout << solve(eq);
}

int main() {
  solve("input.in");
}
