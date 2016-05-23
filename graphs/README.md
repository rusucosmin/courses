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

###A\*
Graph algorithms - A\* algorithm

Problem

Given a graph with non-negative costs, two vertices s and t, and, for each vertex x, an estimation h(x) of the distance from x to t find a minimum cost walk from s to t.

Idea

The goal of the A\* algorithm is to avoid computing paths that start from s but go in a direction opposite to t. For instance, if we want to go from Cluj to Paris, we won't try a route through Moscow.

To be able to exclude such unpromising routes, we need, in addition to the graph itself, an estimation of the distance from each vertex to the target vertex. This estimation is part of the input data.

Of course, not any estimation function will work. There are two conditions on the estimation function:

(strong condition): for all edges (x,y), we have c(x,y) ≥ h(x) - h(y) (in other words, the estimation does not decrease, along an edge, faster than the cost of that edge); in addition, h(t)=0;
(weak condition): for all vertices x, we have h(x) ≤ d(x,t) (in other words, the estimation is always an underestimation).
If the graph represents places in space (cities, intersections, etc), then the estimation function could be the euclidian distance.

Essentially, the A\* algorithm is identical with Dijkstra's algorithm, with one difference: the priority of a vertex x in the priority queue is not dist[x] but rather dist[x]+h(x).
