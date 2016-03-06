// https://www.quora.com/What-is-Knuths-optimization-in-dynamic-programming
#include <iostream>
#include <fstream>
#include <iomanip>
#define DN 3005
#define LL long long
using namespace std;
 
int n,v[DN],m[DN][DN];
LL rez[DN][DN],sp[DN];
 
int main() {
  ifstream f("nucleulvaloros2.in");
  ofstream g("nucleulvaloros2.out");
  f>>n;
  for(int i=1; i<=n; ++i) {
    f>>v[i];
    sp[i]=sp[i-1]+v[i];
  }
  for(int l=0; l<n; ++l)
    for(int i=1; i+l<=n; ++i) {
      int j=i+l;
      if(l==0) {
        rez[i][i]=v[i];
        m[i][i]=i;
        continue;
      }
      /*if(l==1) {
        rez[i][i+1]=min(v[i],v[i+1])+v[i]+v[i+1];
        m[i][i+1]=i;
        continue;
      }*/
      int st=m[i][j-1],dr=m[i+1][j];
      rez[i][j]=(1LL<<60);
      for(int k=max(st-1,i); k<=min(dr+1,j-1); ++k) if(rez[i][j]>rez[i][k]+rez[k+1][j]) {
        rez[i][j]=rez[i][k]+rez[k+1][j];
        m[i][j]=k;
      }
      //for(int k=i; k<j; ++k) rez[i][j]=min(rez[i][j],rez[i][k]+rez[k+1][j]);
      rez[i][j]+=(sp[j]-sp[i-1]);
    }
    /*for(int i=1; i<=n; ++i) {
      for(int j=1; j<=n; ++j) cout<<setw(3)<<rez[i][j]<<' ';
      cout<<'\n';
    }*/
    g<<rez[1][n];
 
}
