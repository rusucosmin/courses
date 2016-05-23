#Exam

##Minimum cost walk by dynamic programming
- Let `dp[k][x] = the minimum cost walk of at most k edges from s to x`
- So `dp[0][s] = 0` and `dp[0][x] = oo for every x != s`
- `dp[k][x] = min({dp[k - 1][y] | (y, x) is an edges in the Graph)`
- Simple c++ code
```c++
memset(dp, oo, sizeof(dp));
dp[0][s] = 0;
for(int k = 1; k < n; ++ k)
    for(int i = 1; i <= n; ++ i)
        for(auto it : gt[node]) /// on the transpose graph. the list gt[node] contains pairs (nextNode, edgeCost)
            dp[k][it.first] = min(dp[k][it.first], dp[k - 1][it.first] + it.second)
/// the solutions lies on dp[n - 1][t]
```

##Bellman-Ford

```c++
#include <bits/stdc++.h>

using namespace std;

const int maxn = 50005;
const int oo = 0x3f3f3f3f;

int main() {
    freopen("bellmanford.in", "r", stdin);
    freopen("bellmanford.out", "w", stdout);
    vector <pair<pair<int, int>, int> > edges;
    int n, m;
    cin >> n >> m;
    vector <int> dist(n + 1, oo);
    while(m --) {
        int x, y, z;
        cin >> x >> y >> z;
        edges.push_back({{x, y}, z});
    }
    dist[1] = 0;
    for(int i = 1; i < n; ++ i) {
        for(auto it : edges)
            if(dist[it.first.second] > dist[it.first.first] + it.second) {
                dist[it.first.second] = dist[it.first.first] + it.second;
            }
    }
    for(auto it : edges)
        if(dist[it.first.second] > dist[it.first.first] + it.second) {
            cout << "Ciclu negativ!\n";
            return 0;
        }
    for(int i = 2 ; i <= n ; ++ i)
        cout << dist[i] << ' ';
}
```

###RoyFloyd

```c++
for(int k = 1; k <= n; ++ k)
    for(int i = 1; i <= n; ++ i)
        for(int j = 1; j <= n; ++ j)
            dp[i][j] = min(dp[i][j], dp[i][k]+ dp[k][j]);
```
