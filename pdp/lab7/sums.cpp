#include <iostream>
#include <fstream>
#include <vector>
#include <thread>
#include <assert.h>

using namespace std;

const int maxlg = 22;
const int maxn = 500005;

int n;
long long dp[maxlg][maxn], sum[maxn], psum[maxn];

const int T = 5;

//#define debug

inline void doIt(int idx) {
  for(int i = idx; i < n; i += T) {
    int act = 0;
    int now = i + 1;
    for(int bit = 0; (1 << bit) <= now; ++ bit) {
      if(now & (1 << bit)) {
        sum[i] += dp[bit][act];
        act += (1 << bit);
      }
    }
  }
}

int main() {
  clock_t t;
  t = clock();

  ifstream fin("sums.in");

  fin >> n;
  for(int i = 0; i < n; ++ i) {
    fin >> dp[0][i];
    psum[i] = psum[i - 1] + dp[0][i];
  }
  /// dp[k][i] = sum(a[j]) where i <= j <= i + 2^k - 1

  // dp[k][i] =
  for(int k = 1; (1 << k) < maxn; ++ k) {
    for(int i = 0; i < n; ++ i) {
      dp[k][i] = dp[k - 1][i] + dp[k - 1][i + (1 << (k - 1))];
    }
  }

  vector <thread> th;
  for(int i = 0; i < min(T, n); ++ i) {
    th.push_back(thread(doIt, i));
  }
  for(int i = 0; i < th.size(); ++ i) {
    th[i].join();
  }
  ofstream fout("sums.out");
  for(int i = 0; i < n; ++ i) {
    fout << sum[i] << '\n';
    assert(sum[i] == psum[i]);
  }

  t = clock() - t;
  cout << "Computing partial sums of an array with " << n
      << " elements took me " << t << " cycles (" 
      << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";

  return 0;
}
