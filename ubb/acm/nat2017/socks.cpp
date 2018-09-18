#include <bits/stdc++.h>

using namespace std;

const int maxn = 1005;
const int inf = 0x3f3f3f3f;

int n, k, size[maxn];
string col[maxn];
bitset <maxn> used;

int main() {
  ifstream fin("socks.in");
  ofstream fout("socks.out");

  fin >> n >> k;
  for(int i = 1; i <= n; ++ i) {
    fin >> col[i] >> size[i];
  }
  int sol = 0;
  unordered_map<string, int> cnt_col;
  unordered_map<int, int> cnt_size;
  for(int i = 1; i <= k; ++ i) {
    int cost = inf;
    int which = -1;
    for(int j = 1; j <= n; ++ j) {
      if(used[j])
        continue;
      int cur = cnt_col[col[j]] + cnt_size[size[j]];
      if(cost > cur) {
        cost = cur;
        which = j;
      }
    }
    sol += cost;
    cnt_col[col[which]] ++;
    cnt_size[size[which]] ++;
    fout << sol << '\n';
  }
}
