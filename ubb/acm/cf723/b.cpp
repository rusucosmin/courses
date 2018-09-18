#include <bits/stdc++.h>

//the length of the longest word outside the parentheses (print 0, if there is no word outside the parentheses),
//the number of words inside the parentheses (print 0, if there is no word inside the parentheses).

using namespace std;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    #endif
    int n;
    string s;
    cin >> n >> s;
    bool par = false;
    int begin = -1;
    int ansa = 0;
    int ansb = 0;
   // cerr << s << '\n';
    for(int i = 0; i < s.size(); ++ i) {
        if(s[i] == ')') {
            par = false;
        }
        if(s[i] == '(') {
            par = true;
        }
        if(isalpha(s[i])) {
            int j = i;
            while(i + 1 < s.size() && isalpha(s[i + 1])) {
                ++ i;
            }
            if(!par) ansa = max(ansa, i - j + 1);
            else
                ++ ansb;
        }
    }
    cout << ansa << ' ' << ansb << '\n';
    return 0;
}
