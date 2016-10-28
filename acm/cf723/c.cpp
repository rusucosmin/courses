#include <bits/stdc++.h>

using namespace std;

const int maxn = 2005;
int n, v[maxn], fr[maxn];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    #endif
    int n, m;
    long long sum = 0;

    cin >> n >> m;
    int act = 1, change = 0;
    for(int i = 0; i < n; ++ i) {
        cin >> v[i];
        if(v[i] <= m)
            ++ fr[ v[i] ];
    }
    for(int i = 0; i < n; ++ i) {
        if(v[i] > m) {
            while(act <= m && fr[act] >= n / m) {
                ++ act;
            }
            if(act == m + 1) {
                continue;
            }
            v[i] = act;
            ++ fr[act];
            ++ change;
        }
    }
    for(int i = 1; i <= m; ++ i) {
        if(fr[i] < n / m) {
            change += (n / m - fr[i]);
        }
    }
    cout << n / m << ' ' << change << '\n';
    for(int i = 1; i <= m; ++ i) {
        for(int j = 1; j <= fr[i]; ++ j)
            cout << i << ' ';
    }
    return 0;
nt act = 1, change = 0;
~                              | 27     for(int i = 0; i < n; ++ i) `j}
