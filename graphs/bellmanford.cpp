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
    return 0;
}
