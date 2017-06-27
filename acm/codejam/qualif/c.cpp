#include <bits/stdc++.h>
using namespace std;

const int maxn = 100005;

int t, n, k, st[maxn], dr[maxn];
bitset <maxn> used;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    #endif

    cin >> t;

    for(int test = 1; test <= t; ++ test) {
        cin >> n >> k;
        int where, maxdist, maxdist2;
        for(int now = 1; now <= k; ++ now) {
            int lastst = 0, lastdr = n + 1;
            for(int i = 1; i <= n; ++ i) {
                if(!used[i]) {
                    st[i] = i - lastst - 1;
                }
                else {
                    lastst = i;
                }
            }
            for(int i = n; i >= 1; -- i) {
                if(!used[i]) {
                    dr[i] = lastdr - i - 1;
                }
                else {
                    lastdr = i;
                }
            }
//            cerr << now << '\n';
//            for(int i = 1; i <= n; ++ i)
//                cerr << st[i] << ' ' << dr[i] << '\n';
//            cerr << '\n';
            where = -1, maxdist = -1, maxdist2 = -1;
            for(int i = 1; i <= n; ++ i) {
                if(used[i])
                    continue;
                int dist = min(st[i], dr[i]);
                if(maxdist < dist) {
                    maxdist = dist;
                    maxdist2 = max(st[i], dr[i]);
                    where = i;
                } else if(maxdist == dist && maxdist2 < max(st[i], dr[i])) {
                    maxdist2 = max(st[i], dr[i]);
                    where = i;
                }
            }
//            cerr << "acum: " << where << '\n';
            assert(where != -1);
            used[where] = 1;
        }
        cout << "Case #" << test << ": ";
        cout << maxdist2 << ' ' << maxdist << '\n';
        used.reset();
    }
}
