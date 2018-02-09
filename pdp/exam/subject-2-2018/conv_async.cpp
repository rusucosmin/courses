#include <iostream>
#include <vector>
#include <thread>

using namespace std;

inline void solve(vector <int> a, vector <int> b, int T) {
  vector <thread> threads;
  int n = a.size();
  vector <int> sol(n, 0);
  for(int idx = 0; idx < T; ++ idx) {
    threads.push_back(thread([a, b, idx, n, &sol, T](){
      for(int i = idx; i < n; i += T) {
        for(int j = 0; j < n; ++ j) {
          sol[i] += a[j] * b[(i - j + n) % n];
        }
      }
    }));
  }
  for(int i = 0; i < threads.size(); ++ i) {
    threads[i].join();
  }
  for(auto it : sol) {
    cerr << it << '\n';
  }
}

int main() {
  solve({1, 2, 3}, {1, 2, 3}, 3);
  // r[0] = a[0] * b[0] + a[1] * b[2] + a[2] * b[1] = 1 * 1 + 2 * 3 + 3 * 2 = 1 + 6 + 6 = 13
  // r[1] = a[0] * b[1] + a[1] * b[0] + a[2] * b[2] = 1 * 2 + 2 * 1 + 3 * 3 = 2 + 2 + 9 = 13
  // r[2] = a[0] * b[2] + a[1] * b[1] + a[2] * b[0] = 1 * 3 + 2 * 2 + 3 * 1 = 3 + 4 + 3 = 10
}
