#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <set>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cmath>
#define DN 2005
#define LL long long
#define x first
#define y second

using namespace std;

struct pt{
	int x,y,id;
} p[DN];
int n,sx,sy;

bool cmp(pt a, pt b) {
	double x=atan2(a.y-sy,a.x-sx),y=atan2(b.y-sy,b.x-sx);
	if(fabs(x-y)<1e-5) {
		if(a.x!=b.x) return a.x<b.x;
		return a.y<b.y;
	}
	return x<y;
}

bool c2(pt a,pt b) {
	if(a.x==b.x) return a.y<b.y;
	return a.x<b.x;
}

int id(pt a,pt b, pt c) {
	return b.x*c.y+c.x*a.y+a.x*b.y-b.x*a.y-c.x*b.y-a.x*c.y <0;
}

int main() {
	//freopen("input.txt","r",stdin);

	cin.sync_with_stdio(false);
	int c;
	for(cin>>c;c--;) {
		cin>>n;
		for(int i=0; i<n; ++i) {
			cin>>p[i].x>>p[i].y;
			p[i].id=i;
		}
		sort(p,p+n,c2);
		vector<pt> ic;
		int fol[DN]; memset(fol,0,sizeof(fol));
		ic.push_back(p[0]); ic.push_back(p[1]);
		fol[p[0].id]=1; fol[p[1].id]=1;
		for(int i=2; i<n; ++i) {
			for(;ic.size()>1 && id(ic[ic.size()-2],ic.back(),p[i]); ic.pop_back()) {
				fol[ic.back().id]=0;
			}
			ic.push_back(p[i]);
			fol[p[i].id]=1;
		}
		for(int i=n-1; i>=0; --i) if(!fol[p[i].id]) ic.push_back(p[i]);
		for(int i=0; i<ic.size(); ++i) cout<<ic[i].id<<' ';
		cout<<'\n';
	}

}