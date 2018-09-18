#include <iostream>
#include <string>
#include <cstdio>
#include <set>
#include <bitset>
#include <algorithm>
#define DN 9999999
#define LL long long
using namespace std;

set<int> fol;
int ind[10],c; 
string s;
bitset<DN+6> isp;

int main() {
	//freopen("input.txt","r",stdin);
	cin.sync_with_stdio(false);
	isp[0]=isp[1]=1;
	for(LL i=2; i*i<=DN; ++i) if(!isp[i])
		for(LL j=i*i; j<=DN; j+=i) isp[j]=1;
	for(cin>>c;c--;) {
		cin>>s;
		int n=s.size();
		fol.clear();
		for(int i=0; i<s.size(); ++i) ind[i]=i;
		do {
			
			for(int j=1; j<(1<<n); ++j) {
				int nr=0;
				for(int i=0; i<n; ++i) if(j&(1<<i)) nr=nr*10+(s[ind[i]]-'0');
				if(!isp[nr]) fol.insert(nr);
			}
			//cerr<<nr<<' ';
			
		}while(next_permutation(ind,ind+n));
		cout<<fol.size()<<'\n';
	}
}