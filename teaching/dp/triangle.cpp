#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 1005;

int n, m, dp[maxn][maxn], a[maxn][maxn];

int main() {
  ifstream fin("triangle.in");

  fin >> n;
  for(int i = 1; i <= n; ++ i) {
    for(int j = 1; j <= i; ++ j) {
      fin >> a[i][j];
    }
  }

  for(int i = 1; i <= n; ++ i) {
    dp[n][i] = a[n][i];
  }

  for(int i = n - 1; i >= 1; -- i) {
    for(int j = 1; j <= i; ++ j) {
      dp[i][j] = a[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1]);
    }
  }

  cout << dp[1][1] << '\n' << 1 << ' ' << 1 << '\n';
  int j = 1;
  for(int i = 2; i <= n; ++ i) {
    if(dp[i][j] < dp[i][j + 1])
      ++ j;
    cout << i << ' ' << j << '\n';
  }
}
