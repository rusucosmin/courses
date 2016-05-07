#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

/**
    The solution is as follows.
    The ballons are moving only vertically. Each circle will stay on a fixed interval [xst, xdr] on the x axis.
    So, each circle will be 'translated' as a closed interval, and the problem is reduced to the Activity Selection Problem.
    http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/

    For simplicity, I will assume we will read the interval [xst, xdr] for each circle.
    If the input will be (r, x, y) - denoting the center (x, y) of the circle and r - the radius, it's easy to get the Ox interval:
        [x-r, x+r]
    Also, I will asume that the circles [1, 2] and [2, 3] do not touch.
*/

class classComp {
public:
    inline bool operator () (const pair<double, double> &a, const pair<double, double> &b) {
        return a.second < b.second;
    }
};

vector <int> baloonSelectionProblem(vector <pair<double, double>> v) {
    if(v.size() == 0)
        return vector <int>();
    sort(v.begin(), v.end(), classComp());
    vector <int> ans;
    int coord = v[0].second;
    ans.push_back(0);
    for(int i = 1 ; i < int(v.size()) ; ++ i) {
        if(v[i].first >= coord) {
            ans.push_back(i);
            coord = v[i].second;
        }
    }
    return ans;
}

int main() {
    ifstream fin("input.in");
    ofstream fout("output.out");

    int n;
    fin >> n;
    vector <pair<double, double> > v;
    for(int i = 0 ; i < n ; ++ i) {
        float st, dr;
        fin >> st >> dr;
        v.push_back(make_pair(st, dr));
    }
    vector <int> ans = baloonSelectionProblem(v);
    fout << ans.size() << '\n';
    for(auto it : ans)
        fout << v[it].first << ' ' << v[it].second << '\n';
    return 0;
}
