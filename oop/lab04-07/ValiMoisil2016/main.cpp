#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("vali.in");
    ofstream fout("vali.out");
    int n, x, cnt1 = 0, cnt2 = 0;
    int p;
    fin >> p;
    if(p == 1) {
        fin >> n;
        for(int i = 1 ; i <= n ; ++ i) {
            int x;
            fin >> x;
            while(x > 9) ///cat timp x mai are cel putin 2cifre
                x = x / 10; /// eliminam ultima cifra
            /// la final x este chiar prima cifra a numarului
            /// initial
            /// 1
            if(x == 1)
                cnt1 ++;
            else
                cnt2 ++;
        }
        ///fout << cnt1 << ' ' << cnt2 << '\n';
        if(cnt1 > cnt2)
            fout << "valentin";
        else
            fout << "valentina";
    }
    else {
        fin >> n;
        long long sum = 0;
        for(int i = 1 ; i <= n ; ++ i) {
            long long x;
            fin >> x;
            long long aux = x;
            long long putere = 1;
            while(aux > 9) {
                aux /= 10;
                putere = putere * 10;
            }
            if(aux == 1) {
                x = x;
                sum = sum + x;
            }
            else {
                x = x - putere;
                sum = sum - x;
            }
        }
        if(sum < 0) {
            long long aux = -sum;
            long long putere = 1;
            while(aux > 9) {
                aux /= 10;
                putere = putere * 10;
            }
            sum = -sum + putere;
        }
        fout << sum << '\n';
    }
    return 0;
}
