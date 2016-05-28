/*
6. Given a digraph with costs, find a minimum cost Hamiltonian cycle (i.e., solve the TSP)
*/
#include <fstream>
#include <iostream>
#include <vector>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <deque>
 
using namespace std;
 
const char infile[] = "hamilton.in";
const char outfile[] = "hamilton.out";
 
ifstream fin(infile);
ofstream fout(outfile);
 
const int MAXN = 18;
const int oo = 0x3f3f3f3f;
 
typedef vector<int> Graph[MAXN];
typedef vector<int> :: iterator It;
 
const inline int min(const int &a, const int &b) { if( a > b ) return b;   return a; }
const inline int max(const int &a, const int &b) { if( a < b ) return b;   return a; }
const inline void Get_min(int &a, const int b)    { if( a > b ) a = b; }
const inline void Get_max(int &a, const int b)    { if( a < b ) a = b; }
 
class DirectedGraph {
private:
    vector <vector <pair<int, int> > > g, gt;
public:
    DirectedGraph(int N) {
        g.resize(N);
        gt.resize(N);
    }
    void addDirectedEdge(int x, int y, int z) {
        g[x].push_back(make_pair(y, z));
        gt[y].push_back(make_pair(x, z));
    }
    /// dp[conf][i] = suntem in nodul si avem vizitate toate nodurile din conf binara a lui conf 10001jjj
    int getMinCostHamiltonianCycle() {
        vector <vector <int> > dp((1 << g.size()), vector <int> (g.size(), oo));
        dp[1][0] = 0;
        int N = g.size();
        int maxMask = (1 << g.size());
        for(int mask = 1 ; mask < maxMask ; ++ mask) {
            for(int i = 0 ; i < N ; ++ i)
                if(mask&(1<<i))
                    for(auto it : gt[i])
                        if(mask & (1 << it.first))
                            dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][it.first] + it.second);
        }
        int ans = oo;
        for(auto it : gt[0])
            ans = min(ans, dp[maxMask - 1][it.first] + it.second);
        return ans;
    }
};
 
int N, M;
 
int main() {
    fin >> N >> M;
    DirectedGraph G(N);
    for(int i = 1 ; i <= M ; ++ i) {
        int x, y, z;
        fin >> x >> y >> z;
        G.addDirectedEdge(x, y, z);
    }
    int ham = G.getMinCostHamiltonianCycle();
    if(ham == oo)
        fout << "Nu exista solutie";
    else
        fout << ham << '\n';
    fin.close();
    fout.close();
    return 0;
}
