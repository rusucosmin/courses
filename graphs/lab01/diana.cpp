#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector <pair<int, int> > g[100];
    int m, n;
    cin  >> n >> m;
    for(int i = 1 ; i <= m ; ++ i) {
        int x, y, z;
        cin >> x >> y >> z;
        g[x].push_back(make_pair(y, z));
    }
    for(int i = 1 ; i <= n ; ++ i) {
        cout << "Lista lui " << i << " estt: ";
        for(int j = 0 ; j < g[i].size() ; ++ j)
            cout << g[i][j].first << ' ' << g[i][j].second << '\n';
        cout << '\n';
    }
}
