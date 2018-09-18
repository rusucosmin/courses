#include <iostream>
#include <fstream>
#include <unordered_map>

using namespace std;

unordered_map<int, int>  fr;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    #endif
    int test, n, d;
    cin >> test;
    while(test --) {
        cin >> d >> n;
        fr.clear();
        fr[0] = 1;
        long long sum = 0;
        long long ans = 0;
        for(int i = 1 ; i <= n ; ++ i) {
            int x;
            cin >> x;
            sum += x;
            ans += fr[sum % d];
            ++ fr[sum % d];
        }
        cout << ans << '\n';
    }

}
