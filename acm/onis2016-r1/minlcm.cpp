#include <iostream>
#include <cassert>
#include <algorithm>
#include <bitset>
#include <fstream>

using namespace std;

const int maxn = 100005;

bitset <maxn> _hash;

int main() {
    freopen("minlcm.in", "r", stdin);
    freopen("minlcm.out", "w", stdout);
    int t;
    cin >> t;
    while(t --) {
        int n;
        cin >> n;
        _hash.reset();
        for(int i = 1 ; i <= n ; ++ i) {
            int x;
            cin >> x;
            _hash[x] = 1;
        }
        long long ans = (1LL << 60);
        for(int d = 1 ; d < maxn ; ++ d) {
            int nr1 = -1, nr2 = -1;
            for(int nxt = d ; nxt < maxn ; nxt += d) {
                if(_hash[nxt]) {
                    if(nr1 == -1)
                        nr1 = nxt;
                    else {
                        nr2 = nxt;
                        break;
                    }
                }
            }
            if(nr1 == -1 || nr2 == -1)
                continue;
            ans = min(ans, (1LL * nr1 * nr2) / __gcd(nr1, nr2));
        }
        cout << ans << '\n';
    }
}
