#include <iostream>
#include <bitset>
#include <algorithm>
#include <fstream>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int maxn = 100005;

set<int> g[maxn], stnodes;
int n, m, when[maxn], tmp, deg[maxn];
map<pair<int, int>, int> matrix;

const int dx[] = {0, 1, 0,-1};
const int dy[] = {1, 0,-1, 0};

void chain() {
}

bool inside(int x, int y) {
    return x >= 1 && y >= 1 && x <= n && y <= m;
}

bool cmp(int a, int b) {
    int mina = 0x3f3f3f3f;
    int minb = 0x3f3f3f3f;
    for(auto it : g[a])
        if(when[it])
            mina = min(mina, when[it]);
    for(auto it : g[b])
        if(when[it])
            minb = min(minb, when[it]);
    return mina < minb || (mina == minb && deg[a] < deg[b]);
}

int ampus;

ofstream fout("puzzle2.out");

bool ala_bun(int node) {
    int cnt = 0;
    for(auto it : g[node])
        if(when[node] > 0)
            ++ cnt;
    return cnt >= 2;
}

void doLine(int node, int maxdeg) {
    fout << node << ' ';
    when[node] = ++ ampus;
    if(deg[node] == 2)
        return ;
    for(auto it : g[node]) {
        if(when[it])
            continue;
        if(deg[it] - maxdeg == 0) {
            doLine(it, maxdeg);
        }
     }
}

void chain(int node) {
    when[node] = 1;
    fout << node << ' ';
    for(auto it : g[node])
        if(!when[it])
            chain(it);
}

bitset<maxn> used;

#include <cassert>

int nextNode(int actnode) {
    vector <int> good;
    for(auto it : g[actnode]) {
        if(!used[it] && (deg[it] == 2 || deg[it] == 3 || deg[it] == 1))
            good.push_back(it);
    }
    sort(good.begin(), good.end(), cmp);
    assert(good.size() > 0);
    return good[0];
}

int main() {
    ifstream fin("puzzle2.in");
    fin >> n >> m;
    if(n == 1) {
        fout << "1 1\n1";
        return 0;
    }
    for(int i = 1 ; i <= m ; ++ i) {
        int x, y;
        fin >> x >> y;
        g[x].insert(y);
        ++ deg[x];
        ++ deg[y];
        g[y].insert(x);
    }
    int mindeg = 4;
    int actnode = 0;
    for(int i = 1 ; i <= n ; ++ i) {
        if(g[i].size() < mindeg) {
            mindeg = g[i].size();
            actnode = i;
        }
    }
    if(mindeg == 1) {
        fout << 1 << ' ' << n << '\n';
        chain(actnode);
        return 0;
    }
    vector <vector <int> > matrix;
    int crt = 0;
    while(ampus < n) {
        vector <int> linie;
        linie.push_back(actnode);
        used[actnode] = 1;
        when[actnode] = ++ ampus;
        int toEnd = deg[actnode];
        do {
            actnode = nextNode(actnode);
            used[actnode] = 1;
            when[actnode] = ++ ampus;
            linie.push_back(actnode);
        } while(deg[actnode] != toEnd);
        matrix.push_back(linie);
        actnode = -1;
        for(auto it : linie) {
            for(auto jt : g[it])
                if(!used[jt]) {
                    -- deg[jt];
                    if((deg[jt] == 2 || deg[jt] == 1) && actnode == -1)
                        actnode = jt;
                }
        }
    }
    fout << matrix.size() << ' ' << matrix[0].size() << '\n';
    for(auto it : matrix) {
        for(auto el : it) {
            fout << el << ' ';
        }
        fout << '\n';
    }
}
