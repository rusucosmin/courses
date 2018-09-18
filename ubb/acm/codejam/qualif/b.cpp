#include <bits/stdc++.h>
using namespace std;

vector <int> getDigits(long long n) {
    vector <int> v;
    while(n > 0) {
        v.push_back(n % 10);
        n /= 10;
    }
    reverse(v.begin(), v.end());
    return v;
}

inline void predecesor(int i, vector <int> &d) {
    if(i == 0) {
        -- d[i];
        return ;
    }
    -- d[i];
    if(d[i] < d[i - 1]) {
        d[i] = 9;
        predecesor(i - 1, d);
    }
}

inline bool tidy(long long nr) {
    int last = 10;
    while(nr > 0) {
        if(nr % 10 > last)
            return false;
        last = nr % 10;
        nr /= 10;
    }
    return true;
}

inline long long brute(long long n) {
    while(!tidy(n))
        -- n;
    return n;
}

inline long long solve(long long n) {
    vector <int> d = getDigits(n);
    long long nr = 0;
    for(int i = 1; i < d.size(); ++ i)
        if(d[i] < d[i - 1]) {
            predecesor(i - 1, d);
            for(int j = i; j < d.size(); ++ j)
                d[j]= 9;
            break;
        }
    for(int i = 0; i < d.size(); ++ i)
        nr = nr * 10 + d[i];
    return nr;
}
 
int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    #endif

    srand(time(NULL));

/*
    for(long long _ = 1; _ <= 10000000; ++ _) {
        long long i = (1LL * rand()) % 100000000000LL + 1;
        long long _ans = solve(i);
        long long _brute = brute(i);
        cerr << i << ' ' <<  _ans << ' ' << _brute << '\n';
        assert(_ans == _brute);
    }
    */

    int t;
    cin >> t;
    for(int test = 1; test <= t; ++ test) {
        cout << "Case #" << test << ": ";
        long long n;
        cin >> n;
        cout << solve(n) << '\n';
    }
}
