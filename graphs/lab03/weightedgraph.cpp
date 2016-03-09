/*
    1. Write a program that, given a graph with positive costs and two vertices, finds a lowest cost walk 
                between the given vertices, using the Dijkstra algorithm.
        http://www.infoarena.ro/job_detail/1638771
    2B. Write a program that, given a graph that has no cycles (a directed acyclic graph, DAG) and a pair of vertices, finds the number of distinct walks between the given vertices.
*/

#include <fstream>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class DirectedGraph {
public:
    static const int oo = 0x3f3f3f3f;
    DirectedGraph() {
    }
    DirectedGraph(string filename) {
        ifstream fin(filename.c_str());
        int n, m;
        fin >> n >> m;
        this->vertices = n;
        this->edges = m;
        g.resize(n);
        for(int i = 0 ; i < m ; ++ i ){
            int x, y, z;
            fin >> x >> y >> z;
            -- x;
            -- y;
            this->addEdge(x, y, z);
        }
        fin.close();
    }
    void addEdge(int x, int y, int z) {
        g[x].push_back(make_pair(y, z));
    }
    vector <int> Dijkstra(int source) {
        vector <int> dist(this->vertices, oo);
        dist[source] = 0;
        priority_queue <pair<int, int>, vector <pair<int, int>>, greater <pair<int, int> > > Q;
        for(Q.push(make_pair(dist[source], source)) ; !Q.empty() ; ) {
           int node = Q.top().second;
           int cost = Q.top().first;
           Q.pop();
           if(dist[node] < cost)
                continue;
           for(auto it : g[node])
                if(dist[it.first] > cost + it.second) {
                    dist[it.first] = cost + it.second;
                    Q.push(make_pair(dist[it.first], it.first));
                }
        }
        return dist;
    }
private:
    vector <vector <pair<int, int>>> g;
    int vertices, edges;
};

int main() {
    DirectedGraph G("dijkstra.in");
    ofstream fout("dijkstra.out");
    vector <int> ans = G.Dijkstra(0);
    for(int i = 1 ; i < static_cast<int>(ans.size()) ; ++ i) {
        if(ans[i] == G.oo)
            ans[i] = 0;
        fout << ans[i] << ' ';
    }
    fout.close();
    return 0;
}
