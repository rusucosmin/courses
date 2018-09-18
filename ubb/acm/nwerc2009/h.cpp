#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <set>
#include <vector>
#include <bitset>
#include <algorithm>
#define DN 10005
#define LL long long
using namespace std;

vector<int> gr[DN*20];
int vl[DN],fr[DN];

int main() {
	//freopen("input.txt","r",stdin);
	cin.sync_with_stdio(false);
	for(int i=2; i<=7; ++i) {
		gr[1].push_back(i);
		gr[i].push_back(1);
	}
	vl[1]=fr[1]=1;
	fr[0]=(1<<30);

	int lst=7;
	for(int i=2; i<DN; ++i) {
		gr[i].push_back(i+1);
		gr[i+1].push_back(i);
		for(;gr[i].size()<6; ++lst) {
			gr[i].push_back(lst); 
			gr[lst].push_back(i);
			//cerr<<i<<' '<<lst<<'\n';
		}
		int fol[6]; memset(fol,0,sizeof(fol));
		for(int j=0; j<gr[i].size(); ++j) if(gr[i][j]<i) {
			fol[vl[gr[i][j]]]=1;
		}
		int v=0;
		for(int j=1; j<=5; ++j) if(!fol[j] && fr[j]<fr[v]) v=j;
		vl[i]=v; ++fr[v];
		--lst;
		//cout<<i<<' '<<v<<'\n';
	}
	int c;
	for(cin>>c;c--;) {
		int n; cin>>n;
		cout<<vl[n]<<'\n';
	}
	
}