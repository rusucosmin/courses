/**
 *
 *
 */

#include <bits/stdc++.h>

using namespace std;

int main() {
  ifstream fin("gap.in");
  ofstream fout("gap.out");
  long long x;
  cin >> x;
  vector <int> d;
  while(x > 0) {
    d.push_back(x % 10);
    x /= 10;
  }
  sort(d.begin(), d.end(), greater<int>());
  long long mare = d[0];
  for(int i = d.size() - 1; i > 0; -- i) {
    mare = mare * 10 + d[i];
  }
  vector<int> uniq(d.size());
  unique(d.begin(), d.end(), uniq.begin());
}
