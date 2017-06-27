#include <bits/stdc++.h>
using namespace std;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    freopen("output_a_small.out", "w", stdout);
    #endif

    cin.sync_with_stdio(false);
    int t;
    cin >> t;
    for(int tst = 1; tst <= t; ++ tst) {
        string s; int k;
        cin >> s >> k;
        int cnt = 0;
        for(int i = 0; i + k - 1 < s.size(); ++ i)
            if(s[i]== '-') {
                ++ cnt;
                for(int j = i; j < i + k; ++ j)
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
            }
        bool ok = true;
        for(int i = 0; i < s.size(); ++ i)
            if(s[i] == '-')
                ok = false;
        cout << "Case #" << tst << ": ";
        if(ok) {
            cout << cnt << '\n';
        }
        else
            cout << "IMPOSSIBLE\n";
    }
}
