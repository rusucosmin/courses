#include <iostream>
#include <fstream>
#include <thread>
#include <vector>
#include <cassert>
#include <chrono>

using namespace std;

const int MAXN = 2001;
const int MAXT[] = {1, 3, 10, 30, 100, 300, 1000};

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

void addLines(int line, int T) {
  // adds line, line + T, line + 2 * T...
  for(int i = line; i < n; i += T) {
    for(int j = 0; j < m; ++ j) {
      c[i][j] = a[i][j] + b[i][j];
    }
  }
}

inline void addMat(int T, bool check = false) {
  auto start = std::chrono::high_resolution_clock::now();
  vector <thread> threads;
  loadData<int>(a, b, "add2.in");
  cerr << "Matrix of dimension " << n << '\n';

  for(int i = 0; i < min(T, n); ++ i) {
    threads.push_back(thread(addLines, i, T));
  }
  for(int i = 0; i < min(T, n); ++ i) {
    threads[i].join();
  }
  if (check) {
    for(int i = 0; i < n; ++ i) {
      for(int j = 0; j < m; ++ j) {
        assert(c[i][j] == a[i][j] + b[i][j]);
        cerr << c[i][j] << ' ';
      }
      cerr << '\n';
    }
  }
  auto finish = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> elapsed = finish - start;
  cerr << "Elapsed time: " << elapsed.count() << '\n';
}

inline void statistics() {
  for(int i = 0; i < 7; ++ i) {
    int t = MAXT[i];
    cerr << t << " threads\n";
    addMat(t);
  }
}

int main() {
  statistics();
  return 0;
}
