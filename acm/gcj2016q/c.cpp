#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

int t, n, J;

int getDiv(int x) {
    for(int d = 2 ; d * d <= x ; ++ d)
        if(x % d == 0)
            return d;
    return 0;
}

inline int conv(string x, int base) {
    int ret = 0;
    for(int i = 0 ; i < x.size() ; ++ i)
        ret = ret * base + x[i] - '0';
    return ret;
}

vector<int> check(string x) {
    vector <int> v;
    //cerr << x << ":\n";
    for(int i = 2 ; i <= 10 ; ++ i) {
        //cerr << conv(x, i) << ' ';
        int aux = getDiv(conv(x, i));
        //cerr << aux << '\n';
        if(aux == 0)
            return vector <int> ();
        v.push_back(aux);
    }
    return v;
}

void back(string x) {
    if(x.size() == n - 1) {
        x = x + "1";
        vector <int> divi = check(x);
        if(divi.size() != 0) {
            cout << x << ' ';
            for(auto it : divi)
                cout << it << ' ';
            cout << '\n';
            -- J;
            if(J == 0)
                exit(1);
        }
        return ;
    }
    back(x + "0");
    back(x + "1");
}

int main() {
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    cin >> t;
    for(int test = 1 ; test <= t ; ++ test) {
        cout << "Case #" << test << ":\n";
        cin >> n >> J;
        back("1");
    }
}
