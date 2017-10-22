#include <iostream>
#include <fstream>
#include <thread>
#include <vector>
#include <cassert>

using namespace std;

const int MAXN = 1000;
const int T = 1000;

int n, m, k;
int a[MAXN][MAXN], b[MAXN][MAXN], c[MAXN][MAXN];

template <class T>
void loadData(T a[MAXN][MAXN], T b[MAXN][MAXN], string fileName) {
  ifstream fin(fileName);
  fin >> n >> m >> k;
  for(int i = 0; i < n ;++ i) {
    for(int j = 0; j < m; ++ j) {
      fin >> a[i][j];
    }
  }
  for(int i = 0; i < m ;++ i) {
    for(int j = 0; j < k; ++ j) {
      fin >> b[i][j];
    }
  }
}

void multLines(int line) {
  // mults line, line + T, line + 2 * T...
  memset(c, 0, sizeof(c));
  for(int i = line; i < n; i += T) {
    for(int j = 0; j < m; ++ j) {
      for(int l = 0; l < k; ++ l) {
          c[i][l] += a[i][j] * b[j][l];
      }
    }
  }
}

int main() {
  vector <thread> threads;
  loadData<int>(a, b, "mult.in");

  for(int i = 0; i < min(T, n); ++ i) {
    threads.push_back(thread(multLines, i));
  }
  for(int i = 0; i < min(T, n); ++ i) {
    threads[i].join();
  }
  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < m; ++ j) {
//      assert(c[i][j] == a[i][j] + b[i][j]);
      cerr << c[i][j] << ' ';
    }
    cerr << '\n';
  }
  return 0;
}
