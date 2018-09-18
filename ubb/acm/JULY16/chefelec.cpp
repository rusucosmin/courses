#include <iostream>
#include <fstream>
#include <queue>
#include <string.h>
#include <cassert>

using namespace std;

const int maxn = 100005;
const long long inf = 1LL * 0x3f3f3f3f * 0x3f3f3f3f;

long long dp[maxn];
int x[maxn], dad[maxn];

int main() {
    #ifdef home
    freopen("input.in", "r", stdin);
    #endif
    int t;
    cin >> t;
    while(t --) {
        int n;
        string light;
        priority_queue <pair<long long, int> > q;
        cin >> n;
        cin >> light;
        for(int i = 0; i < n; ++ i) {
            dad[i] = 0;
            dp[i] = inf;
            cin >> x[i];
            if(light[i] == '1')
                q.push(make_pair(0, i)),
                dp[i] = 0,
                dad[i] = i;
        }
        long long sum = 0;
        while(!q.empty()) {
            long long cost = -q.top().first;
            int node = q.top().second;
            q.pop();
            if(node != 0)
                if(dp[node - 1] > cost + x[node] - x[node - 1]) {
                    dp[node - 1] = cost + x[node] - x[node - 1];
                    dad[node - 1] = node;
                    q.push(make_pair(-dp[node - 1], node - 1));
                }
            if(node != n - 1)
                if(dp[node + 1] > cost + x[node + 1] - x[node]) {
                    dp[node + 1] = cost + x[node + 1] - x[node];
                    dad[node + 1] = node;
                    q.push(make_pair(-dp[node + 1], node + 1));
                }
        }
        for(int i = 0; i < n; ++ i)
            sum += max(x[i] - x[ dad[i] ], x[ dad[i] ] - x[i]);
        assert(sum != inf);
        cout << sum << '\n';
    }
}
