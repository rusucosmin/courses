#include <iostream>
#include <fstream>
#include <vector>
#include <thread>

using namespace std;

int n;
vector <vector <int>> a, b, c;

inline void solve(int T) {
  vector <thread> t;
  for(int idx = 0; idx < T; ++ idx) {
    t.push_back(thread([&, idx, T](){
      for(int i = idx; i < n; i += T) {
        for(int j = 0; j < n; ++ j) {
          for(int k = 0; k < n; ++ k) {
            c[i][j] += a[i][k] * b[k][j];
          }
        }
      }
    }));
  }
  for(int i = 0; i < t.size(); ++ i) {
    t[i].join();
  }
}

int main() {
  ifstream fin("input.in");

  fin >> n;

  for(int i = 0; i < n; ++ i) {
    a.push_back(vector <int> ());
    c.push_back(vector <int> ());
    for(int j = 0; j < n; ++ j) {
      int x;
      fin >> x;
      a.back().push_back(x);
      c.back().push_back(0);
    }
  }
  for(int i = 0; i < n; ++ i) {
    b.push_back(vector <int>() );
    for(int j = 0; j < n; ++ j) {
      int x;
      fin >> x;
      b.back().push_back(x);
    }
  }


  solve(5);

  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < n; ++ j) {
      cerr << c[i][j] << ' ';
    }
    cerr << '\n';
  }
}
