#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

#define t first
#define d second

const int maxn = 205;

vector <pair<int, int> > q[2];
int dp[maxn][maxn][2];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    #endif
    int test;
    cin >> test;
    while(test -- ) {
        int n;
        cin >> n;
        q[0].push_back(make_pair(0, 0));
        q[1].push_back(make_pair(0, 0));
        for(int i = 1 ; i <= n ; ++ i) {
            char c;
            int t, d;
            cin >> c >> t >> d;
            q[c - 'A'].push_back(make_pair(t, d));
        }
        memset(dp, 0x3f3f3f3f, sizeof(dp));
        n = q[0].size() - 1;
        int m = q[1].size() - 1;
        dp[0][1][1] = q[1][1].t + q[1][1].d;
        dp[1][0][0] = q[0][1].t + q[0][1].d;
        for(int i = 1 ; i <= n ; ++ i)
            for(int j = 1 ; j <= m ; ++ j) {
                dp[i][j][0] = max(dp[i - 1][j][1], q[0][i].t) + q[0][i].d;
                dp[i][j][1] = max(dp[i][j - 1][0], q[1][j].t) + q[1][j].d;
                if(i >= 2)
                    dp[i][j][0] = min(dp[i][j][0], max(dp[i - 1][j][0] + 10, max(q[0][i].t, dp[i - 1][j][0] - q[0][i - 1].d + 10) + q[0][i].d));
                if(j >= 2)
                    dp[i][j][1] = min(dp[i][j][1], max(dp[i][j - 1][1] + 10, max(q[1][j].t, dp[i][j - 1][1] - q[1][j - 1].d + 10) + q[1][j].d));
            }
        cout << min(dp[n][m][0], dp[n][m][1]) << '\n';
        q[0].clear();
        q[1].clear();
    }
}
