/**
    1B. Write a program that finds the strongly-connected components of a directed graph in O(n+m) (n=no. of vertices, m=no. of arcs)
        http://www.infoarena.ro/job_detail/1638713
*/

#include <iostream>
#include <vector>
#include <stack>
#include <fstream>

using namespace std;

class DirectedGraph {
public:
    DirectedGraph() {
    }
    DirectedGraph(string filename) {
        ifstream fin(filename.c_str());
        int n, m;
        fin >> n >> m;
        this->vertices = n;
        this->edges = m;
        this->g.resize(n);
        this->gt.resize(n);
        for(int i = 0 ; i < m ; ++ i) {
            int x, y;
            fin >> x >> y;
            -- x;
            -- y;
            this->addEdge(x, y);
        }
    }
    void addEdge(int x, int y) {
        this->g[x].push_back(y);
        this->gt[y].push_back(x);
    }
    vector <vector <int> > getStronglyConnectedCompoentents() {
        return tarjanAlgorithm();
    }
private:
    vector <vector <int> > tarjanAlgorithm() {
        int index = 0;
        vector <vector<int> > scc;
        vector <int> lowlink(this->vertices, 0), level(this->vertices, 0);
        stack <int> st;
        vector <bool> inst(this->vertices, false);
        for(int i = 0 ; i < vertices ; ++ i)
            if(!lowlink[i])
                tarjanDf(i, level, lowlink, index, st, inst, scc);
        return scc;
    }
    vector <int> getCc(int node, stack <int> &st, vector <bool> &inst) {
        int act;
        vector <int> v;
        do {
            inst[act = st.top()] = 0;
            st.pop();
            v.push_back(act);
        }while(act != node);
        return v;
    }
    void tarjanDf(int node, vector <int> &level, vector <int>  &lowlink, int &index,
                        stack<int> &st, vector <bool> &inst, vector <vector <int> > &bcc) {
        lowlink[node] = level[node] = ++ index;
        st.push(node);
        inst[node] = 1;
        for(auto it : g[node]) {
            if(!lowlink[it]) {
                tarjanDf(it, level, lowlink, index, st, inst, bcc);
                lowlink[node] = min(lowlink[node], lowlink[it]);
            } else if(inst[it])
                lowlink[node] = min(lowlink[node], lowlink[it]);
        }
       if(lowlink[node] == level[node])
            bcc.push_back(getCc(node, st, inst));
    }
    int vertices, edges;
    vector <vector <int> > g, gt;
};

int main() {
    DirectedGraph g("ctc.in");
    ofstream fout("ctc.out");
    vector <vector <int> > scc = g.getStronglyConnectedCompoentents();
    cerr << scc.size() << '\n';
    for(auto it : scc) {
        for(auto el : it)
            cerr << el + 1 << ' ';
        cerr << '\n';
    }
}
