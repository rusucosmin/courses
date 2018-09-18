#include <bits/stdc++.h>

using namespace std;

const int maxn = 100005;
const int maxg = 16;
const int mod = 1000000007;

int p[maxg], t, n, sum[maxn], q[maxg], putere[maxn];

inline int getSum(int conf) {
  int ret = 1;
  for(int i = 0; i < n; ++ i) {
    if(!(conf & (1 << i))) { //avem 0
      ret = (1LL * ret * sum[i]) % mod;
    }
    else
      ret = (1LL * ret * putere[i]) % mod;
  }
  return ret;
}

inline int cnt(int conf) {
  int ret = 1;
  for(int i = 0; i < n; ++ i) {
    if(!(conf & (1 << i))) { //avem 0
      ret = (1LL * ret * (q[i] + 1)) % mod;
    }
  }
  return ret;
}

int main() {
  freopen("input.in", "r", stdin);

  cin >> t;
  for(int tst = 1; tst <= t; ++ tst) {
    cin >> n;
    for(int i = 0; i < n; ++ i) {
      cin >> p[i] >> q[i];
      putere[i] = 1;
      sum[i] = 1;
      for(int j = 1; j <= q[i]; ++ j) {
        putere[i] = (1LL * putere[i] * p[i]) % mod;
        sum[i] = (1LL * sum[i] + putere[i]) % mod;
      }
    }
    long long res = 1;
    for(int a = 0; a < (1 << n); ++ a) {
      int b = 0;
      for(int i = 0; i < n; ++ i)
        if(!(a & (1 << i)))
          b |= (1 << i);
      if(a > b)
        continue;
     // cerr << a << ' ' << b << '\n';
     int suma = (1LL * getSum(a) * cnt(b)) % mod;
     int sumb = (1LL * getSum(b) * cnt(a)) % mod;
//     res = (1LL * res * (suma + sumb) * (cnt(a) + cnt(b))) % mod;
     // cerr << getSum(a) << ' ' << cnt(a) << ' ' << getSum(b) << ' ' << cnt(b) << '\n';
      res = (1LL * suma + sumb) % mod;
     // cerr << "res, suma, sumb: " << res << ' ' << suma << ' ' << sumb << '\n';
      //res = (1LL * ((1LL * res * getSum(a)) % mod) * getSum(b)) % mod;
    }
    cout << "Case " << tst << ": " << res << '\n';
  }
}
