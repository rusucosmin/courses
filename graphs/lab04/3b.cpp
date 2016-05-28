/// 3B
#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <queue>

using namespace std;

class DirectedGraph {
    public:
    DirectedGraph(string filename) {
        ifstream fin(filename.c_str());
        int n, m;
        fin >> n >> m;
        this->vertices = n;
        this->edges = m;
        g.resize(n);
        while(m --) {
            int x, y, z;
            fin >> x >> y >> z;
            g[x].push_back(make_pair(y, z));
        }
    }
    vector <int> tsortDfs() {
        vector <int> ret;
        vector <bool> used(this->vertices, false);
        for(int i = 0 ; i < this->vertices ; ++ i)
            if(!used[i])
                dfs(i, used, ret);
        reverse(ret.begin(), ret.end());
        return ret;
    }
    int nrOfMinPaths(int x, int y) {
        vector <int> dp(this->vertices, 0x3f3f3f3f);
        vector <int> cnt(this->vertices, 0);
        dp[x] = 0;
        cnt[x] = 1;
        for(auto el : this->tsortDfs()) {
            if(dp[el] == -0x3f3f3f3f)
                continue;
            for(auto it : g[el]) {
                if(dp[it.first] > dp[el] + it.second) {
                    dp[it.first] = dp[el] + it.second;
                    cnt[it.first] = cnt[el];
                }
                else if(dp[it.first] == dp[el] + it.second) {
                    cnt[it.first] += cnt[el];
                }
            }
        }
        return cnt[y];
    }
    bool isDag() {
        return int(tsortDfs().size()) == this->vertices;
    }
    private:
    void dfs(int node, vector <bool> &used, vector <int> &ret) {
        used[node] = 1;
        for(auto it : g[node])
            if(!used[it.first])
                dfs(it.first, used, ret);
        ret.push_back(node);
    }
    vector <vector <pair<int, int>>> g;
    int vertices, edges;
};

int main() {
    DirectedGraph g("3b.in");
    if(!g.isDag()) {
        cerr << "Not a dag\n";
        return 0;
    }
    cerr << g.nrOfMinPaths(0, 4) << '\n';
}
