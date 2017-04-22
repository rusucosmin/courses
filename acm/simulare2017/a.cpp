#include <bits/stdc++.h>
using namespace std;

const int maxn = 505;
const int inf = 0x3f3f3f3f;

vector <int> g[maxn];
int lowlink[maxn], dflevel[maxn];
bitset<maxn> used;
int ans, n, m;

inline void dfs(int node, int dad, int level) {
  used[node] = 1;
  lowlink[node] = dflevel[node] = level;
  for(auto it : g[node]) {
    if(it == dad)
      continue;
    if(!used[it]) {
      dfs(it, node, level + 1);
      //lowlink[node] = min(lowlink[node], lowlink[it]);
    }
    else {
      //lowlink[node] = min(lowlink[node], dflevel[it]);
      if(dflevel[it] < level) {
        ans = min(ans, level - dflevel[it] + 1);
      }
    }
  }
}

const int lim = (1 << 20);
char buff[lim];
int pos;

inline int getInt() {
  int nr = 0;
  while(buff[pos] < '0' || buff[pos] > '9') {
    if(++ pos == lim) {
      pos = 0;
      fread(buff, 1, lim, stdin);
    }
  }
  while(buff[pos] >= '0' && buff[pos] <= '9') {
    nr = nr * 10 + buff[pos] - '0';
    if(++ pos == lim) {
      pos = 0;
      fread(buff, 1, lim, stdin);
    }
  }
  return nr;
}

int main() {
  //freopen("input.in", "r", stdin);
  int t;
  t = getInt();
  //cin >> t;
  for(int tst = 1; tst <= t; ++ tst) {
    ans = inf;
    n = getInt();
    m = getInt();
    //cin >> n >> m;
    for(int i = 0; i < m; ++ i) {
      int x, y;
      x = getInt();
      y = getInt();
      //cin >> x >> y;
      g[x].push_back(y);
      g[y].push_back(x);
    }

    for(int i = 0; i < n; ++ i)
      if(!used[i])
        dfs(i, i, 1);


    if(ans == inf || n <= 2 || ans <= 2)
      cout << "Case " << tst << ": impossible\n";
    else
      cout << "Case " << tst << ": " << ans << '\n';
    for(int i = 0; i < n; ++ i) {
      vector<int>().swap(g[i]);
      lowlink[i] = 0;
      dflevel[i] = 0;
      used[i] = 0;
    }
  }
}
