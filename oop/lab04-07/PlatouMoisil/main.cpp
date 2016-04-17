#include <iostream>
#include <fstream>

using namespace std;

int main()
{int n, x, xprec, fr, maxfr, nrmax;
    ifstream fin("platou.in");
    ofstream fout("platou.out");
    fin >> n;
    fin >> xprec;
    fr = 1;
    maxfr = 1;
    nrmax = xprec;
    for(int i=2;i<=n;i++)
    {
        fin >> x;
        if(x == xprec)
            fr ++;
        else
            fr = 1;
        if(maxfr < fr) {
            maxfr = fr;
            nrmax = x;
        }
        else if(maxfr == fr)
            if(nrmax < x)
                nrmax = x;
        xprec = x;
    }
    fout << maxfr << ' ' << nrmax << '\n';
    return 0;
}
