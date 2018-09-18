#include <bits/stdc++.h>

using namespace std;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    #endif
    int v[3];
    cin >> v[0] >> v[1] >> v[2];
    sort(v, v + 3);
    cout << v[1] - v[0] + v[2] - v[1] << '\n';
    return 0;
}
