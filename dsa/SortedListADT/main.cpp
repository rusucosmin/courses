#include <iostream>
#include <fstream>
#include <tester.h>
#include <sortedsllist.h>
#include <abstractsortedlist.h>
#include <sortedlistbst.h>
#include <ctime>

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
    double coord = v->getAtIndex(0).first;
    ans.push_back(0);
    for(int i = 1 ; i < int(v->size()) ; ++ i) {
        if(v->getAtIndex(i).second >= coord) {
            ans.push_back(i);
            coord = v->getAtIndex(i).first;
        }
    }
    return ans;
}

vector <int> baloonSelectionProblem(vector <pair<double, double>> v) {
    if(v.size() == 0)
        return vector <int>();
    vector <int> ans;
    double coord = v[0].second;
    ans.push_back(0);
    for(int i = 1 ; i < int(v.size()) ; ++ i) {
        if(v[i].first >= coord) {
            ans.push_back(i);
            coord = v[i].second;
        }
    }
    return ans;
}

void solveSLList(string input, string output, string okfile) {
    ifstream fin(input);
    ofstream fout(output);
    ifstream fok(okfile);
    int n;
    fin >> n;
    SortedSLList <pair<double, double> > v;
    for(int i = 0 ; i < n ; ++ i) {
        double st, dr;
        fin >> st >> dr;
        v.add(make_pair(dr, st));
    }
    vector <int> ans = baloonSelectionProblem(&v);
    int sol;
    fok >> sol;
    assert(sol == ans.size());
    fout << ans.size() << '\n';
    for(auto it : ans)
        fout << v.getAtIndex(it).first << ' ' << v.getAtIndex(it).second << '\n';
}

void solveSLBST(string input, string output, string okfile) {
    ifstream fin(input);
    ofstream fout(output);
    ifstream fok(okfile);
    int n;
    fin >> n;
    SortedListBST <pair<double, double> > v;
    for(int i = 0 ; i < n ; ++ i) {
        double st, dr;
        fin >> st >> dr;
        v.add(make_pair(dr, st));
    }
    vector <int> ans = baloonSelectionProblem(&v);
    int sol;
    fok >> sol;
    assert(sol == ans.size());
    fout << ans.size() << '\n';
    for(auto it : ans)
        fout << v.getAtIndex(it).first << ' ' << v.getAtIndex(it).second << '\n';
}

void solveVector(string input, string output, string okfile) {
    ifstream fin(input);
    ofstream fout(output);
    ifstream fok(okfile);
    int n;
    fin >> n;
    vector <pair<double, double> > v;
    for(int i = 0 ; i < n ; ++ i) {
        double st, dr;
        fin >> st >> dr;
        v.push_back(make_pair(st, dr));
    }
    sort(v.begin(), v.end(),
         [] (const pair<double, double> &a, const pair<int, int> &b) -> bool
         {
             return a.second < b.second;
         });
    vector <int> ans = baloonSelectionProblem(v);
    int sol;
    fok >> sol;
    assert(sol == ans.size());
    fout << ans.size() << '\n';
    for(auto it : ans)
        fout << v[it].first << ' ' << v[it].second << '\n';
}

void blackBoxTest() {
    cout << "---------------------------------------\n";
    cout << "Running tests using vector as container\n";
    cout << "---------------------------------------\n";
    for(int i = 0; i < 20; ++ i) {
        clock_t st = clock();
        solveVector("tests/test" + to_string(i) + ".in", "tests/test" + to_string(i) + ".out", "tests/test" + to_string(i) + ".ok");
        clock_t fn = clock();
        double elapsed_secs = double(fn - st) / CLOCKS_PER_SEC;
        cout << "Test " << i << " took " << elapsed_secs << " seconds\n";
    }

    cout << "----------------------------------------------\n";
    cout << "Running tests using SortedListBST as container\n";
    cout << "----------------------------------------------\n";
    for(int i = 0; i < 20; ++ i) {
        clock_t st = clock();
        solveSLBST("tests/test" + to_string(i) + ".in", "tests/test" + to_string(i) + ".out", "tests/test" + to_string(i) + ".ok");
        clock_t fn = clock();
        double elapsed_secs = double(fn - st) / CLOCKS_PER_SEC;
        cout << "Test " << i << " took " << elapsed_secs << " seconds\n";
    }

    cout << "---------------------------------------------\n";
    cout << "Running tests using SortedSLList as container\n";
    cout << "---------------------------------------------\n";
    for(int i = 0; i < 7; ++ i) {
        clock_t st = clock();
        solveSLList("tests/test" + to_string(i) + ".in", "tests/test" + to_string(i) + ".out", "tests/test" + to_string(i) + ".ok");
        clock_t fn = clock();
        double elapsed_secs = double(fn - st) / CLOCKS_PER_SEC;
        cout << "Test " << i << " took " << elapsed_secs << " seconds\n";
    }
}

int main() {
    blackBoxTest();
    return 0;
}
