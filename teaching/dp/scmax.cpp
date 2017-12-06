#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 100005;

int n, dp[maxn], a[maxn], urm[maxn];

int main() {
  ifstream fin("scmax.in");

  fin >> n;
  for(int i = 1; i <= n; ++ i) {
    fin >> a[i];
  }


  // compute dp
  for(int i = n; i >= 1; -- i) {
    dp[i] = 1;
    urm[i] = -1;
    for(int j = i + 1; j <= n; ++ j) {
      if(a[i] < a[j] && dp[j] + 1 > dp[i]) {
        dp[i] = dp[j] + 1;
        urm[i] = j;
      }
    }
  }

  int pozmax = 1;
  // find the starting point
  for(int i = 2; i <= n; ++ i) {
    if(dp[pozmax] < dp[i]) {
      pozmax = i;
    }
  }

  cout << dp[pozmax] << '\n';

  for(int i = pozmax; i != -1; i = urm[i]) {
    cout << a[i] << ' ';
  }
}
