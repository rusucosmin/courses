#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 2005;

int n, m, a[maxn], b[maxn];

int main() {
    ifstream fin("maxsubsum.in");
    ofstream fout("maxsubsum.out");

    fin >> n >> m;
    for(int i = 1 ; i <= n ; ++ i)
        fin >> a[i];
    for(int i = 1 ; i <= m ; ++ i)
        fin >> b[i];

    long long ssma = 0, actsum = 0;
    int st = 1;
    int lga = 0;
    for(int i = 1 ; i <= n ; ++ i) {
        if(actsum < 0) {
            actsum = a[i];
            st = i;
        }
        else
            actsum += a[i];
        if(actsum > ssma) {
            ssma = actsum;
            lga = i - st + 1;
        }
        else if(actsum == ssma) {
            lga = max(lga, i - st + 1);
        }
    }
    long long ssmb = 0;
    actsum = 0;
    st = 1;
    int lgb = 0;
    for(int i = 1 ; i <= m ; ++ i) {
        if(actsum < 0) {
            actsum = b[i];
            st = i;
        }
        else
            actsum += b[i];
        if(actsum > ssmb) {
            ssmb = actsum;
            lgb = i - st + 1;
        }
        else if(actsum == ssmb) {
            lgb = max(lgb, i - st + 1);
        }
    }

    /// suppose A
    long long ans = 0;
    for(int i = 1 ; i <= m ; ++ i) {
        int sum = 0;
        for(int j = i ; j <= m ; ++ j) {
            sum += b[j];
            ans = max(ans, ssma * (j - i + 1) + sum * lga);
        }
    }
    for(int i = 1 ; i <= n ; ++ i) {
        int sum = 0;
        for(int j = i ; j <= n ; ++ j) {
            sum += a[j];
            ans = max(ans, sum * lgb + ssmb * (j - i + 1));
        }
    }
    fout << ans << '\n';
}
