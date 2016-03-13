#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

const int maxn = 50005;

vector<pair<int, int> > g[maxn];
int test, n, m;
long long sus[maxn], jos[maxn];
int sumfr[maxn], fr[maxn];

void dfsjos(int node, int father) {
    sumfr[node] = fr[node];
    jos[node] = 0;
    for(auto it : g[node]) {
        if(it.first == father)
            continue;
        dfsjos(it.first, node);
        sumfr[node] += sumfr[it.first];
        jos[node] = jos[node] + jos[it.first] + 1LL * it.second * (sumfr[it.first]);
    }
}

void dfssus(int node, int father) {
    for(auto it : g[node]) {
        if(it.first == father)
            continue;
        sus[it.first] = sus[node] + 1LL * it.second * (sumfr[1] - sumfr[it.first])
                        + (jos[node] - jos[it.first] - 1LL * it.second * sumfr[it.first]);
        dfssus(it.first, node);
    }
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    #endif

    cin >> test;
    while(test --) {
        cin >> n;
        for(int i = 1 ; i < n;  ++ i) {
            int x, y, z;
            cin >> x >> y >> z;
            z = 2*z;
            g[x].push_back(make_pair(y, z));
            g[y].push_back(make_pair(x, z));
        }
        cin >> m;
        for(int i = 1 ; i <= m ; ++ i) {
            int x, y;
            cin >> x >> y;
            fr[x] = y;
        }
        dfsjos(1, 0);
        dfssus(1, 0);
        long long ans = (1LL << 60);
        for(int i = 1 ; i <= n ; ++ i) {
            ans = min(ans, sus[i] + jos[i]);
        }
        cout << ans << '\n';
        for(int i = 1 ; i <= n; ++ i)
            if(sus[i] + jos[i] == ans)
                cout << i << ' ';
        cout << '\n';
        for(int i = 1 ; i <= n ; ++ i) {
            vector <pair<int, int> > ().swap(g[i]);
        }
        memset(sumfr, 0, sizeof(sumfr));
        memset(jos, 0, sizeof(jos));
        memset(sus, 0, sizeof(sus));
        memset(fr, 0, sizeof(fr));
    }
}
