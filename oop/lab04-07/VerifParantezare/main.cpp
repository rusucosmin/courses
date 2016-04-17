#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("parantezare.in");
    ofstream fout("parantezare.out");
    int n, sum = 0, x;
    int corect = 1;
    fin >> n;
    for(int i = 1 ; i <= n ; ++ i) {
        fin >> x;
        if(x == 0)
            ++ sum;
        else
            -- sum;
        if(sum < 0) /// este negativa => sirul e parantezat
            corect = 0;
    }
    if(sum != 0)
        corect = 0;
    if(corect == 1)
        fout << "corect\n";
    else
        fout << "incorect\n";
    return 0;
}
