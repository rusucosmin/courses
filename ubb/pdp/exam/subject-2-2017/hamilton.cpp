#include <iostream>
#include <fstream>
#include <vector>
#include <thread>

using namespace std;

const int maxn = 1005;

int n, m;

bool solved = false;
vector <int> sol;
vector <int> g[maxn];

inline void back(vector <int> nodes, int T) {
  if(solved) {
    return ;
  }
  if(nodes.size() == n) {
    if(!solved) {
      solved = true;
      sol = nodes;
    }
    return ;
  }
  if(T > 1) {
    vector <int> adj = g[nodes.back()];
    thread t([adj, nodes, T](){
      cerr << "new thread\n";
      for(int i = 0; i < adj.size(); i += 2) {
        if(find(nodes.begin(), nodes.end(), adj[i]) == nodes.end()) {
          vector <int> aux(nodes);
          aux.push_back(adj[i]);
          back(aux, T / 2);
        }
      }
    });
    for(int i = 1; i < adj.size(); i += 2) {
      if(find(nodes.begin(), nodes.end(), adj[i]) == nodes.end()) {
        vector <int> aux(nodes);
        aux.push_back(adj[i]);
        back(aux, T - T / 2);
      }
    }
    t.join();
  } else {
    for(auto it : g[nodes.back()]) {
      if(find(nodes.begin(), nodes.end(), it) == nodes.end()) {
        vector <int> aux(nodes);
        aux.push_back(it);
        back(aux, T);
      }
    }
  }
}

int main() {
  ifstream fin("input.in");
  ofstream fout("output.out");
  fin >> n >> m;

  for(int i = 0; i < m; ++ i) {
    int x, y;
    fin >> x >> y;
    g[x].push_back(y);
    g[y].push_back(x);
  }
  vector <int> init;
  init.push_back(1);
  back(init, 6);
  if(!solved) {
    cout << "Not found!\n";
  } else {
    for(auto it : sol) {
      cout << it << '\n';
      fout << it << '\n';
    }
  }
}
