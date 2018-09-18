#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class DirectedAcyclicGraph {
public:
    DirectedAcyclicGraph() {
    }
    DirectedAcyclicGraph(string fileName) {
        ifstream fin(fileName.c_str());
        fin >> this-> n >> this->m;
        g.resize(n);
        gt.resize(n);
        for(int i = 1 ; i <= m ; ++ i) {
            int x, y;
            fin >> x >> y;
            -- x;
            -- y;
            this->addEdge(x, y);
        }
    }
    int getNumberOfPaths(int x, int y) {
        vector <bool> used(this->n);
        vector <int> dp(this->n);
        dfs(x, dp, used);
        return dp[y];
    }
    void addEdge(int x, int y) {
        g[x].push_back(y);
        gt[y].push_back(x);
    }
private:
    vector <vector <int> > g, gt;
    int n, m;
    void dfs(int node, vector <int> &dp, vector <bool> &used) {
        used[node] = 1;
        dp[node] = 1;
        for(auto it : g[node])
            if(!used[it]) {
                dfs(it, dp, used);
                dp[it] += dp[node];
            }
            else {
                dp[it] += dp[node];
            }
    }
};

int main() {
    DirectedAcyclicGraph g("dag.in");
    cerr << g.getNumberOfPaths(0, 3) << '\n';
}
