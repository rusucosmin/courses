#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
#include <fstream>
#include <set>
#include <bitset>

using namespace std;

const int maxn = 100005;
const int oo = 0x3f3f3f3f;

vector <int> g[maxn];
int n, m, diam[maxn], diamup[maxn], up[maxn], depth[maxn];

inline void dfs_down(int node, int father) {
  depth[node] = 0;
  diam[node] = 0;
  int max1 = -1, max2 = -1;
  for(auto it : g[node]) {
    if(it == father)
      continue;
    dfs_down(it, node);
    depth[node] = max(depth[node], depth[it] + 1);
    diam[node] = max(diam[node], diam[it]);
    if(max1 < depth[it]) {
      max2 = max1;
      max1 = depth[it];
    }
    else if(max2 < depth[it]) {
      max2 = depth[it];
    }
  }
  diam[node] = max(diam[node], max1 + max2 + 2);
}

void dfs_up(int node, int father) {
  int _max = -2;
  for(auto it : g[node]) {
    if(it == father)
      continue;
    up[it] = max(up[it], up[node] + 1);
    up[it] = max(up[it], _max + 2);
    _max = max(_max, depth[it]);
  }
  _max = -2;
  for(auto it = g[node].rbegin() ; it != g[node].rend() ; ++ it) {
    if(*it == father)
      continue;
    up[*it] = max(up[*it], _max + 2);
    _max = max(_max, depth[*it]);
  }
  for(auto it : g[node]) {
    if(it == father)
      continue;
    dfs_up(it, node);
  }
}

void dfs_diam(int node, int father) {
  int _max = 0;
  multiset <int> ms;
  /// cazul in sus + restul fiilor
  for(auto it : g[node]) {
    if(it == father)
      continue;
    ms.insert(-(depth[it] + 1));
    diamup[it] = max(diamup[it], diamup[node]);   /// cazul in sus...
    diamup[it] = max(diamup[it], _max);
    _max = max(_max, diam[it]);
  }
  _max = 0;
  for(auto it = g[node].rbegin() ; it != g[node].rend() ; ++ it) {
    if(*it == father)
      continue;
    diamup[*it] = max(diamup[*it], _max);
    _max = max(_max, diam[*it]);
  }
  ms.insert(-up[node]);
  for(auto it : g[node]) {
    if(it == father)
      continue;
    ms.erase(ms.find(-(depth[it] + 1)));
    if(ms.size() == 1)
      diamup[it] = max(diamup[it], -*ms.begin());
    else if(ms.size() >= 2) {
      auto its = ms.begin();
      int sum = *its;
      ++ its;
      sum += *its;
      diamup[it] = max(diamup[it], -sum);
    }
    ms.insert(-(depth[it] + 1));
  }
  for(auto it : g[node]) {
    if(it == father)
      continue;   
    dfs_diam(it, node);
  }
}

int main() {
  ifstream fin("revolta.in");
  ofstream fout("revolta.out");
  int t;
  fin >> t;
  while(t --) {
    fin >> n;
    for(int i = 0; i + 1 < n; ++ i) {
      int x, y;
      fin >> x >> y;
      ++ x; ++ y;
      g[x].push_back(y);
      g[y].push_back(x);
    }
    dfs_down(1, 0);
    dfs_up(1, 0);
    dfs_diam(1, 0);
    int ans = diam[1];
    for(int i = 2; i <= n; ++ i) {
      ans = min(ans, 1 + ((diam[i] + 1) / 2) + ((diamup[i] + 1) / 2));
    }
    fout << ans << '\n';
    multiset<int> ms;
    for(int i = 1; i <= n; ++ i)
      vector <int>().swap(g[i]);
    memset(diam, 0, sizeof(diam));
    memset(diamup, 0, sizeof(diamup));
    memset(up, 0, sizeof(up));
    memset(depth, 0, sizeof(depth));
  }
}
