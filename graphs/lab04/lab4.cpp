/// http://www.infoarena.ro/job_detail/1694021?action=view-source

/// 3 and 4
/// Lab 4
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
            -- x; -- y;
            g[x].push_back(make_pair(y, z));
        }
    }
    vector <int> tsortQ() {
        queue <int> q;
        vector <int> deg(this->vertices, 0);
        for(int i = 0 ; i < this->vertices; ++ i) {
            for(auto it : g[i])
                ++ deg[it.first];
        }
        for(int i = 0 ; i < this->vertices ; ++ i)
            if(!deg[i])
                q.push(i);
        vector <int> ret;
        while(!q.empty()) {
            int node = q.front();
            ret.push_back(node);
            q.pop();
            for(auto it : g[node])
                if(--deg[it.first] == 0)
                    q.push(it.first);
        }
        return ret;
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
    int longestPath(int x, int y) {
        vector <int> dp(this->vertices, -0x3f3f3f3f);
        dp[x] = 0;
        for(auto el : this->tsortDfs()) {
            if(dp[el] == -0x3f3f3f3f)
                continue;
            for(auto node : g[el])
                dp[node.first] = max(dp[node.first], dp[el] + node.second);
        }
        return dp[y];
    }
    bool isDag() {
        return int(tsortQ().size()) == this->vertices;
    }
    private:
    void dfs(int node, vector <bool> &used, vector <int> &ret) {
        used[node] = 1;
        for(auto it : g[node])
            if(!used[it.first])
                dfs(it.first, used, ret);
        ret.push_back(node);
    }
    vector <vector <pair<int, int> > > g;
    int vertices, edges;
};

int main() {
    DirectedGraph g("sortaret.in");
    ofstream fout("sortaret.out");
    if(!g.isDag()) {
        fout << "Not a dag\n";
        return 0;
    }
    for(auto it : g.tsortDfs())
        fout << it + 1 << ' ';
    fout << g.longestPath(0, 1) << '\n';
    fout << g.longestPath(2, 8) << '\n';
}
