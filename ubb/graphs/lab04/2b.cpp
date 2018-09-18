/// 2B
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
            int x, y;
            fin >> x >> y;
            g[x].push_back(y);
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
    int nrOfPaths(int x, int y) {
        vector <int> dp(this->vertices, 0);
        dp[x] = 1;
        for(auto el : this->tsortDfs()) {
            if(dp[el] == -0x3f3f3f3f)
                continue;
            for(auto node : g[el])
                dp[node] += dp[el];
        }
        return dp[y];
    }
    bool isDag() {
        return int(tsortDfs().size()) == this->vertices;
    }
    private:
    void dfs(int node, vector <bool> &used, vector <int> &ret) {
        used[node] = 1;
        for(auto it : g[node])
            if(!used[it])
                dfs(it, used, ret);
        ret.push_back(node);
    }
    vector <vector <int> > g;
    int vertices, edges;
};

int main() {
    DirectedGraph g("2b.in");
    if(!g.isDag()) {
        cerr << "Not a dag\n";
        return 0;
    }
    cerr << g.nrOfPaths(0, 4) << '\n';
}
