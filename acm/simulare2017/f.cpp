#include <bits/stdc++.h>

using namespace std;

const int maxn = 105;

int t, n, m, up[maxn][maxn], lft[maxn][maxn], what[maxn][maxn], cuplat[maxn * maxn], pereche[maxn * maxn];
int upNodes, lftNodes;
vector <int> g[maxn * maxn];
bitset <maxn * maxn> used;

inline int dfs(int node) {
  if(used[node])
    return 0;
  used[node] = 1;
  for(auto it : g[node]) {
    if(!cuplat[it]) {
      //cerr << "for1: " << node << ' ' << it << '\n';
      cuplat[it] = node;
      pereche[node] = it;
      return 1;
    }
  }
  for(auto it : g[node]) {
    if(dfs(cuplat[it])) {
      //cerr << "for2: " << node << ' ' << it << '\n';
      cuplat[it] = node;
      pereche[node] = it;
      return 1;
    }
  }
  return 0;
}

inline int cuplaj() {
  int cnt = 0;
  bool ok = true;
  while(ok) {
    ok = false;
    for(int i = 1; i <= upNodes; ++ i) {
      if(!pereche[i]) {
//        cerr << "intra " << i << '\n';
        ok |= dfs(i);
      }
    }
//    for(int i = 1; i <= upNodes; ++ i)
//      cerr << "pereche: " << i << ' ' << pereche[i] << '\n';
    used.reset();
  }
  for(int i = 1; i <= upNodes; ++ i) {
    if(pereche[i]) {
//      cerr << "cuplat " << i << ' ' << pereche[i] << '\n';
      ++ cnt;
    }
  }
  return cnt;
}

int main() {
///  freopen("input.in", "r", stdin);
  cin >> t;
  for(int tst = 1; tst <= t; ++ tst) {
    cin >> n >> m;
    int p;
    cin >> p;
    for(int i = 0; i < p; ++ i) {
      int x, y;
      cin >> x >> y;
      what[x][y] = 1;
    }
    cin >> p;
    for(int i = 0; i < p; ++ i) {
      int x, y;
      cin >> x >> y;
      what[x][y] = -1;
    }
    for(int i = 1; i <= n; ++ i)
      for(int j = 1; j <= m; ++ j)
        if(what[i][j] == -1)
          up[i][j] = 0;
        else if(up[i - 1][j] == 0)
          up[i][j] = ++ upNodes;
        else
          up[i][j] = up[i - 1][j];
    for(int i = 1; i <= n; ++ i)
      for(int j = 1; j <= m; ++ j)
        if(what[i][j] == -1)
          lft[i][j] = 0;
        else if(lft[i][j - 1] == 0)
          lft[i][j] = ++ lftNodes;
        else
          lft[i][j] = lft[i][j - 1];
/*
    for(int i = 1; i <= n; ++ i, cerr << '\n')
      for(int j = 1; j <= m; ++ j)
        cerr << up[i][j] << ' ';

    for(int i = 1; i <= n; ++ i, cerr << '\n')
      for(int j = 1; j <= m; ++ j)
        cerr << lft[i][j] << ' ';
        */

    for(int i = 1; i <= n; ++ i)
      for(int j = 1; j <= m; ++ j)
        if(what[i][j] == 1) {
          g[up[i][j]].push_back(lft[i][j]);
          ///cerr << "edge " << up[i][j] << ' ' << lft[i][j] << '\n';
        }

    cout << cuplaj() << '\n';

    for(int i = 1; i <= upNodes; ++ i)
      vector <int> ().swap(g[i]);
    upNodes = 0;
    lftNodes = 0;
    memset(up, 0, sizeof(up));
    memset(lft, 0, sizeof(lft));
    memset(what, 0, sizeof(what));
    memset(cuplat, 0, sizeof(cuplat));
    memset(pereche, 0, sizeof(pereche));
    used.reset();
  }
}
