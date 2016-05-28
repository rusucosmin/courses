#include <iostream>
#include <bitset>
#include <vector>
#include <string.h>
#include <queue>
#include <fstream>

using namespace std;
/*
NEW(TODO): 1B. Write a program that, given a graph with costs, having no negative cost cycles, and a pair of vertices, finds the number of distinct walks of minimum cost between the given vertices.
*/

const int maxn = 100005;
const int oo = 0x3f3f3f3f;

vector <pair<int, int> > g[maxn];
vector <int> dag[maxn];
int n, m, st, fn, dist[maxn], dp[maxn];
bitset <maxn> used;

inline void dijkstra() {
    priority_queue <pair<int, int>, vector <pair<int, int> >, greater<pair<int, int> > > q;
    memset(dist, oo, sizeof(dist));
    dist[st] = 0;
    q.push(make_pair(0, st));
    while(!q.empty()) {
        int node = q.top().second;
        int cost = q.top().first;
        q.pop();
        if(node == fn)
            return ;
        if(dist[node] != cost)
            continue;
        for(auto it : g[node]) {
            if(dist[it.first] > cost + it.second) {
                dist[it.first] = cost + it.second;
                q.push(make_pair(dist[it.first], it.first));
            }
        }
    }
}

void build_dag() {
    for(int i = 1; i <= n; ++ i) {
        for(auto it : g[i]) {
            if(dist[it.first] == dist[i] + it.second) {
                dag[i].push_back(it.first);
                cerr << i << ' ' << it.first << '\n';
            }
        }
    }
}

void dfs(int node) {
    used[node] = 1;
    for(auto it : dag[node])
        if(!used[it])
            dfs(it);
    for(auto it : dag[node])
        dp[node] += dp[it];
}

void solve() {
    dp[fn] = 1;
    for(int i = 1; i <= n; ++ i)
        if(!used[i])
            dfs(i);
    cout << dp[node] << '\n';
}

int main() {

    ifstream fin("input.in");

    fin >> n >> m >> st >> fn;
    for(int i = 1; i <= m; ++ i) {
        int x, y, z;
        fin >> x >> y >> z;
        g[x].push_back(make_pair(y, z));
    }
    dijkstra();
    build_dag();
    solve();
}
