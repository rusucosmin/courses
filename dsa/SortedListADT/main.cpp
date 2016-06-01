#include <iostream>
#include <fstream>
#include <tester.h>
#include <sortedsllist.h>
#include <abstractsortedlist.h>
#include <sortedlistbst.h>

using namespace std;

/**
    The solution is as follows.
    The ballons are moving only vertically. Each circle will stay on a fixed interval [xst, xdr] on the x axis.
    So, each circle will be 'translated' as a closed interval, and the problem is reduced to the Activity Selection Problem.
    http://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/
    For simplicity, I will assume we will read the interval [xst, xdr] for each circle.
    If the input will be (r, x, y) - denoting the center (x, y) of the circle and r - the radius, it's easy to get the Ox interval:
        [x-r, x+r]
    Also, I will assume that the circles [1, 2] and [2, 3] do not touch.
*/

class classComp {
public:
    inline bool operator () (const pair<double, double> &a, const pair<double, double> &b) {
        return a.second < b.second;
    }
};

vector <int> baloonSelectionProblem(AbstractSortedList <pair<double, double>> *v) {
    if(v->size() == 0)
        return vector <int>();
    vector <int> ans;
    int coord = v->getAtIndex(0).first;
    ans.push_back(0);
    for(int i = 1 ; i < int(v->size()) ; ++ i) {
        if(v->getAtIndex(i).second >= coord) {
            ans.push_back(i);
            coord = v->getAtIndex(i).first;
        }
    }
    return ans;
}

int main() {
    ifstream fin("input.in");
    ofstream fout("output.out");

    int n;
    fin >> n;
    SortedListBST <pair<double, double> > v;
    SortedSLList <pair<double, double> > s;
    for(int i = 0 ; i < n ; ++ i) {
        double st, dr;
        fin >> st >> dr;
        v.add(make_pair(dr, st));
        s.add(make_pair(dr, st));
    }
    for(int i = 0 ; i < v.size() ; ++ i)
        cout << v.getAtIndex(i).first << ' ' << v.getAtIndex(i).second << '\n';
    for(int i = 0 ; i < s.size() ; ++ i)
        cout << s.getAtIndex(i).first << ' ' << s.getAtIndex(i).second << '\n';
    vector <int> ans = baloonSelectionProblem(&v);
    vector <int> ans2 = baloonSelectionProblem(&s);
    assert(ans == ans2);
    fout << ans.size() << '\n';
    for(auto it : ans)
        fout << v.getAtIndex(it).first << ' ' << v.getAtIndex(it).second << '\n';
    return 0;
}
