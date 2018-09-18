nclude <iostream>
#include <fstream>
#include <set>
#include <algorithm>
#define DM 90005
#define DQ 120005
#define DN 30005
#define LL long long
#define x first
#define y second
#define mp make_pair
#define MLT (1LL<<60)
using namespace std;
 
typedef pair<LL,LL> per;
 
int n,m,k;
LL dmin[DN];
 
struct av {
  int a,ta,b,tb,cst;
} a[DM];
struct qu {
  int d,t;
} q[DQ];
int ib[DQ];
LL rez[DQ];
 
bool _2(int x,int y) {
  return q[x].t<q[y].t;
}
 
set<pair<per,per> > ev;//(timp,at/dec) (idx,cst)
 
void prav(av a) {
  cout<<a.a<<' '<<a.ta<<' '<<a.b<<' '<<a.tb<<' '<<a.cst<<'\n';
}
 
int main() {
  ifstream f("avioane2.in");
  ofstream g("avioane2.out");
  f>>n>>m>>k;
  for(int i=0; i<m; ++i) {
    f>>a[i].a>>a[i].ta>>a[i].b>>a[i].tb>>a[i].cst;
    ev.insert(mp(mp(a[i].ta,1),mp(i,0)));
  }
  for(int i=0; i<k; ++i) {
    f>>q[i].d>>q[i].t;
    ib[i]=i;
  }
  sort(ib,ib+k,_2);
  //for(int i=0; i<m; ++i) cout<<a[ia[i]].a<<' '<<a[ia[i]].ta<<' '<<a[ia[i]].b<<' '<<a[ia[i]].tb<<' '<<a[ia[i]].cst<<'\n';
  for(int i=2; i<=n; ++i) dmin[i]=MLT;
  for(int i=0,j=0; i<k; ++i) {
    int tm=q[ib[i]].t;
    //cout<<tm<<":\n";
    for(;ev.size() && ev.begin()->x.x<=tm; ) {
      int tp=ev.begin()->x.y,idx=ev.begin()->y.x;
     // cout<<tp<<' '; prav(a[idx]);
      LL cst=ev.begin()->y.y;
      ev.erase(ev.begin());
      av _av=a[idx];
      if(tp==1 && dmin[_av.a]!=MLT)
        ev.insert(mp(mp(_av.tb,-1),mp(idx,dmin[_av.a])));
      else if(tp==-1) 
        dmin[_av.b]=min(dmin[_av.b],cst+_av.cst);
    }
    int dst=q[ib[i]].d;
    rez[ib[i]]=dmin[dst];
    //cout<<"REZ:"<<dst<<' '<<dmin[dst]<<'\n';
  }
  for(int i=0; i<k; ++i)
    if(rez[i]==MLT) g<<"-1\n";
    else g<<rez[i]<<'\n';
}
