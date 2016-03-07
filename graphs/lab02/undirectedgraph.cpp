/**
    3. Write a program that finds the connected components of an undirected graph using a depth-first traversal of the graph.
        http://www.infoarena.ro/job_detail/1638429
    4. Write a program that finds the connected components of an undirected graph using a breadth-first traversal of the graph.
        http://www.infoarena.ro/job_detail/1638417

    2B. Write a program that finds the biconnected components of an undirected graph in O(n+m).
        http://www.infoarena.ro/job_detail/1638544
*/
#include <iostream>
#include <queue>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

/**
    UndirectedGraph class to encapsulate the data for a graph.
    Contains:
        the neighbours list for each vertex

*/
class UndirectedGraph {
public:
    UndirectedGraph() {
    }
    UndirectedGraph(string fileName) {
        ifstream fin(fileName.c_str());
        int n, m;
        fin >> n >> m;
        this->vertices = n;
        this->edges = m;
        this->g.resize(this->vertices);
        for(int i = 0 ; i < this->edges; ++ i) {
            int x, y;
            fin >> x >> y;
            -- x;
            -- y;
            this->addEdge(x, y);
            this->addEdge(y, x);
        }
    }
    void addEdge(int x, int y) {
        this->g[x].push_back(y);
    }
    int getNoVertices() {
        return this->vertices;
    }
    int getNoEdges() {
        return this->edges;
    }
    vector <vector <int> > getConnectedComponentsDfs() {
        vector <vector <int> > cc;
        vector <bool> visited(this->vertices, false);
        for(int i = 0 ; i < this->vertices ; ++ i)
            if(!visited[i]) {
                vector <int> act;
                _dfs(i, visited, act);
                cc.push_back(act);
            }
        return cc;
    }
    vector <vector <int> > getConnectedComponentsBfs() {
        vector <bool> visited(this->vertices, false);
        vector <vector <int> > cc;
        for(int i = 0 ; i < this->vertices ; ++ i)
            if(!visited[i]) {
                vector <int> act;
                _bfs(i, visited, act);
                cc.push_back(act);
            }
        return cc;
    }
    vector <vector <int> > getBiconnectedComponents() {
        vector <bool> visited(this->vertices, false);
        vector <int> lowlink(this->vertices, 0), father(this->vertices, 0), level(this->vertices, 0);
        stack <pair<int, int> > st;
        vector <vector <int> > bcc;
        _bcDfs(0, visited, lowlink, 0, level, st, bcc);
        return bcc;
    }
    UndirectedGraph deepCopy() {
        UndirectedGraph newg;
        newg.vertices = this->vertices;
        newg.edges = this->edges;
        newg.g = this->g;
        return newg;
    }
private:
    vector <int> _getBc(int x, int y, stack<pair<int, int> > &st) {
        vector <int> act;
        int tx, ty;
        do {
            tx = st.top().first;
            ty = st.top().second;
            st.pop();
            act.push_back(tx);
            act.push_back(ty);
        }while(tx != x || ty != y);
        sort(act.begin(), act.end());
        act.resize(unique(act.begin(), act.end()) - act.begin());
        return act;
    }
    void _bcDfs(int node, vector <bool> &visited, vector <int> &lowlink, int father,
                    vector<int> &level, stack<pair<int, int>> &st, vector <vector <int> > &bcc) {
        level[node] = level[father] + 1;
        lowlink[node] = level[node];
        visited[node] = 1;
        for(auto it : g[node]) {
            if(it == father)
                continue;
            if(!visited[it]) {
                st.push(make_pair(node, it));
                _bcDfs(it, visited, lowlink, node, level, st, bcc);
                lowlink[node] = min(lowlink[node], lowlink[it]);
                if(lowlink[it] >= level[node])
                   bcc.push_back(_getBc(node, it, st));
            }
            else lowlink[node] = min(lowlink[node], level[it]);
        }
    }
    void _dfs(int node, vector <bool> &visited, vector <int> &act) {
        visited[node] = 1;
        act.push_back(node);
        for(auto it : g[node])
            if(!visited[it])
                _dfs(it, visited, act);
    }
    void _bfs(int stnode, vector <bool> &visited, vector <int> &act) {
        queue <int> q;
        q.push(stnode);
        visited[stnode] = 1;
        while(!q.empty()) {
            int node = q.front();
            act.push_back(node);
            q.pop();
            for(auto it : g[node])
                if(!visited[it]) {
                    visited[it] = 1;
                    q.push(it);
                }
        }
    }
    vector <vector <int>> g;
    int vertices, edges;
};

int main() {
    UndirectedGraph g("biconex.in");
    ofstream fout("biconex.out");
    vector <vector <int>>bcc = g.getBiconnectedComponents();
    fout << bcc.size() << '\n';
    for(auto it : bcc) {
        for(auto el : it)
            fout << el + 1 << ' ';
        fout << '\n';
    }
}
