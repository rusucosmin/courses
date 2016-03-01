#include <iostream>
#include <queue>
#include <fstream>
#include <vector>

using namespace std;

/**
    Graph class to encapsulate the data for a graph.
    Contains:
        the neighbours list for each vertex
        the transpose graph (for reverse edges)
    It has an independent class (typename T) for costs.

*/
template <typename T>
class Graph {
public:
    Graph() {
    }
    Graph(string fileName) {
        ifstream fin(fileName.c_str());
        fin >> this->vertices >> this->edges;
        this->g.resize(vertices);
        this->gt.resize(vertices);
        for(int i = 0 ; i < this->edges; ++ i) {
            int x, y, z;
            fin >> x >> y >> z;
            this->addEdge(x, y, z);
        }
    }
    bool setEdgeCost(int x, int y, int z) {
        if(!this->isEdge(x, y))
            return 0;
        for(typename vector <pair<int, T>> :: iterator it = g[x].begin() ; it != g[x].end() ; ++ it)
            if(it->first == y)
                it->second = z;
        for(typename vector <pair<int, T>> :: iterator it = gt[y].begin() ; it != gt[y].end() ; ++ it)
            if(it->first == x)
                it->second = z;
        return 1;
    }
    T getEdgeCost(int x, int y) {
        for(auto it : g[x])
            if(it.first == y)
                return it.second;
        cerr << "NULL\n";
        return NULL;
    }
    bool isEdge(int x, int y) {
        for(auto it : g[x])
            if(it.first == y)
                return 1;
        return 0;
    }
    void addEdge(int x, int y, T z) {
        if(isEdge(x, y))
            return ;
        this->edges ++;
        this->g[x].push_back(make_pair(y, z));
        this->gt[y].push_back(make_pair(x, z));
    }
    int getNoVertices() {
        return this->vertices;
    }
    int getNoEdges() {
        return this->edges;
    }
    int getInDegree(int x) {
        return g[x].size();
    }
    int getOutDegree(int x) {
        return gt[x].size();
    }
    vector <pair<int, T>> getInboundEdges(int x) {
        return g[x];
    }
    vector <pair<int, T>> getOutboundEdges(int x) {
        return gt[x];
    }
    void dfs(int stnode) {
        vector <bool> visited(this->vertices, false);
        _dfs(stnode, visited);
    }
    void bfs(int stnode) {
        vector <bool> visited(this->vertices, false);
        _bfs(stnode, visited);
    }
    Graph<T> deepCopy() {
        Graph newg;
        newg.vertices = this->vertices;
        newg.edges = this->edges;
        newg.g = this->g;
        newg.gt = this->gt;
        return newg;
    }
private:
    void _dfs(int node, vector <bool> &visited) {
        visited[node] = 1;
        for(auto it : g[node])
            if(!visited[it.first])
                _dfs(it.first, visited);
    }
    void _bfs(int stnode, vector <bool> &visited) {
        queue <int> q;
        q.push(stnode);
        visited[stnode] = 1;
        while(!q.empty()) {
            int node = q.front();
            q.pop();
            for(auto it : g[node])
                if(!visited[it.first]) {
                    visited[it.first] = 1;
                    q.push(it.first);
                }
        }
    }
    vector <vector <pair<int, T>>> g, gt;
    int vertices, edges;
};

int main() {
    Graph <int> g("example.txt");
    cerr << g.getNoVertices() << '\n';
    Graph <int> G = g.deepCopy();
}
