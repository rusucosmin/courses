#include <iostream>
#include <fstream>
#include <thread>
#include <vector>
#include <cassert>

using namespace std;

const int MAXN = 1000;
const int T = 1000;

int n, m;
int a[MAXN][MAXN], b[MAXN][MAXN], c[MAXN][MAXN];

template <class T>
void loadData(T a[MAXN][MAXN], T b[MAXN][MAXN], string fileName) {
  ifstream fin(fileName);
  fin >> n >> m;
  for(int i = 0; i < n ;++ i) {
    for(int j = 0; j < m; ++ j) {
      fin >> a[i][j];
    }
  }
  for(int i = 0; i < n ;++ i) {
    for(int j = 0; j < m; ++ j) {
      fin >> b[i][j];
    }
  }
}

void addLines(int line) {
  // adds line, line + T, line + 2 * T...
  for(int i = line; i < n; i += T) {
    for(int j = 0; j < m; ++ j) {
      c[i][j] = a[i][j] + b[i][j];
    }
  }
}

int main() {
  vector <thread> threads;
  loadData<int>(a, b, "add.in");

  for(int i = 0; i < min(T, n); ++ i) {
    threads.push_back(thread(addLines, i));
  }
  for(int i = 0; i < min(T, n); ++ i) {
    threads[i].join();
  }
  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < m; ++ j) {
      assert(c[i][j] == a[i][j] + b[i][j]);
      cerr << c[i][j] << ' ';
    }
    cerr << '\n';
  }
  return 0;
}
