#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector <int> v;
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int test = 1 ; test <= t ; ++ test) {
        int fr = 0;
        long long n;
        cin >> n;
        if(n == 0) {
            cout << "Case #" << test << ": INSOMNIA\n"; 
            continue;
        }
        long long act = n;
        while(fr != ((1 << 10) - 1)) {
            long long cn = act;
            while(cn > 0) {
                fr = fr | (1 << (cn % 10));
                cn = cn / 10;
            }
            act = act + n;
        }
        cout << "Case #" << test << ": ";
        cout << act - n << '\n';
    }
}
