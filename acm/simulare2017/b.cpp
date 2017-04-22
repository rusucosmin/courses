#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <cmath>
#include <map>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#define DN 501
#define DL 11
#define INF (1<<30)
#define x first
#define y second
#define LL long long
#define mp make_pair

using namespace std;


int minflip(string &s, string &t) {
    map<char, map<char, int>> cnt;
    int ns = 0, n1 = 0, n0 = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == t[i])
            continue;
        ++ cnt[s[i]][t[i]];
    }
    if(cnt['1']['0'] > cnt['0']['1'] + cnt['?']['1'])
        return -1;
    int nr = 0;
    int cur = min(cnt['1']['0'], cnt['0']['1']);

    nr += cur;

    cnt['1']['0'] -= cur;
    cnt['0']['1'] -= cur;

    if(cnt['1']['0'] > 0) {
        nr += 2 * cnt['1']['0'];
        cnt['?']['1'] -= cnt['1']['0'];
        cnt['1']['0'] = 0;
    }
    nr += cnt['?']['0'] + cnt['?']['1'] + cnt['0']['1'];
    return nr;
}

int main() {
    int tst;
    string s, t;
    //freopen("input.txt", "r", stdin);
    cin >> tst;
    for (int i = 0; i < tst; ++i) {
        cin >> s >> t;
        cout << "Case " << i+1 << ": " << minflip(s, t) << "\n";
    }
    return 0;
}
