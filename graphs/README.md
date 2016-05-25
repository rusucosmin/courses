#Exam
- Shortest path:
    - BFS x
    - Dijkstra x
    - A\* x
        - Dijkstra with the priority being dist(x) + h(x) x
    - Bellman Ford x
    - Bellman Kalaba x
    - Floyd Warshall x
    - [Matrix multiplication](https://en.wikipedia.org/wiki/Min-plus_matrix_multiplication) x
- Connected Components
    - DFS x
- Strongly connected Components
    - Kosaraju x
    - Tarjan x
- DAGs
    - Topological Sort
        - BFS x
        - DFS x
    - DFS x
    - Critical Path Method (Activity planification)
    - Longest path x
- Minimum spanning tree
    - Kruskal x
    - Prim x
- Maximum Flow
    - Ford Fulkerson 'method' x
    - Edmond Kard – while(bfs()) x
    - Dinic - push every blocking flow (dag of the minimum distances) x
- Maximum Matching

##Minimum cost walk by dynamic programming
- Find minimum cost walk in presence of negative cost edges (but no negative cost cycles).
- Note: if there is a negative cost cycle that can be inserted into the walk from start to end, then there is no minimum cost walk - by repeating the cycle, we can obtain walks of cost as small as we want
- Let s = starting vertex, t = ending (target) vertex.
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
- The algorithm keeps two mappings:
    - dist[x] = the cost of the minimum cost walk from s to x known so far
    - prev[x] = the vertex just before x on the walk above.
- Initially, dist[s]=0 and dist[x]=∞ for x ≠ s; this reflects the fact that we only know a zero-length walk from s to itself.
- Then, we repeatedly performs a relaxation operation defined as follows: if (x,y) is an edge such that dist[y] > dist[x] + c(x,y), then we set:
    - dist[y] = dist[x] + c(x,y)
    - prev[y] = x
- The idea of the relaxation operation is that, if we realize that we have a better walk leading to y by using (x,y) as its last edge, compared to what we know so far, we update our knowledge.

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

###Dijkstra
- Dijkstra's algorithm still relies on Bellman's optimality principle; however, it computes distances from the starting vertex in increasing order of the distances. This way, the distance from start to a given vertex doesn't have to be recomputed after the vertex is processed.
- This way, Dijkstra's algorithm looks a bit like the breadth-first traversal; however, the queue is replaced by a priority queue where the top vertex is the closest to the starting vertex.

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

###Matrix multiplcation
- [wiki](https://en.wikipedia.org/wiki/Min-plus_matrix_multiplication)
