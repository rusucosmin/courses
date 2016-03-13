#include <iostream>
#include <cassert>
#include <cstdio>
#define DN 205
#define LL long long
#define x first
#define y second
using namespace std;

typedef pair<int,int> per;

int c,n,bst[205][205][2],la,lb;
per a[DN],b[DN];


int main() {
  freopen("input.in","r",stdin);
  cin.sync_with_stdio(false);
  for(cin>>c;c--;) {
    la=lb=0;
    for(cin>>n;n--;) {
      char c; int t,d;
      cin>>c>>t>>d;
      if(c=='A') a[++la]=make_pair(t,d);
      else b[++lb]=make_pair(t,d);
    }
    for(int i=0; i<=la; ++i) for(int j=0; j<=lb; ++j) bst[i][j][0]=bst[i][j][1]=(1<<29);
    bst[0][0][0]=bst[0][0][1]=0;
    for(int i=0; i<=la; ++i) for(int j=0; j<=lb; ++j) {
      int smin=bst[i][j][0]-a[i].y,fmin=0;
      for(int jj=j+1; jj<=lb; ++jj) {
        smin=max(smin+10,b[jj].x);
        fmin=max(fmin+10,smin+b[jj].y);
        bst[i][jj][1]=min(bst[i][jj][1],fmin);
      }
      smin=bst[i][j][1]-b[j].y; fmin=0;
      for(int ii=i+1; ii<=la; ++ii) {
        smin=max(smin+10,a[ii].x);
        fmin=max(fmin+10,smin+a[ii].y);
        bst[ii][j][0]=min(bst[ii][j][0],fmin);
      }
    }
    cout<<min(bst[la][lb][0],bst[la][lb][1])<<'\n';
  }
}
