#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 25;

int beat[maxn], tobeat, n, m, ans = 0x3f3f3f3f;

void back(int step, int conf, int bitcnt) {
    if(step == n) {
        if((conf & tobeat) == tobeat && bitcnt < ans) {
            ans = bitcnt;
        }
        return ;
    }
    back(step + 1, conf, bitcnt);
    back(step + 1, conf | beat[step], bitcnt + 1);
}

int main() {
    ifstream fin("pokemon3.in");
    ofstream fout("pokemon3.out");

    fin >> n >> m;
    for(int i = 0 ; i < n ; ++ i)
        for(int j = 0; j < n; ++ j) {
            int x;
            fin >> x;
            if(x)
                beat[i] |= (1 << j);
        }
    for(int i = 0 ; i < m ; ++ i)
        for(int j = 0 ; j < 3 ; ++ j) {
            int x;
            fin >> x;
            -- x;
            tobeat |= (1 << x);
        }
    back(0, 0, 0);
    if(ans == 0x3f3f3f3f)
        fout << "-1\n";
    else
        fout << ans << '\n';
}
