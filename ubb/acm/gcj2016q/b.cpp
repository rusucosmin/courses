#include <iostream>

using namespace std;

int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int test = 1 ; test <= t ; ++ test) {
        string s;
        cin >> s;
        int ans = 0;
        for(int i = 1 ; i < s.size() ; ++ i)
            if(s[i] != s[i - 1])
                ++ ans;
        if(s[s.size() - 1] == '-')
            ++ ans;
        cout << "Case #" << test << ": " << ans << '\n';
    }
}
