#include <iostream>
#include <fstream>
#include <vector>
#include <thread>
#include <atomic>

using namespace std;

atomic <int> cnt;

inline bool check(vector <int> const &v) {
  if(v.size() == 0) {
    return false;
  }
  return v[0] % 2 == 0;
}

inline void generate(vector <int> v, int k, int n, int T) {
  if(v.size() == k) {
    for(auto it : v) {
      cerr << it << ' ';
    }
    cerr << '\n';
    if(check(v)) {
      cnt ++;
    }
    return ;
  }
  int lst = 0;
  if(v.size() > 0) {
    lst = v.back();
  }
  if(T == 1) {
    for(int i = lst + 1; i <= n; ++ i) {
      v.push_back(i);
      generate(v, k, n, T);
      v.pop_back();
    }
  } else {
    thread t([&]() {
      vector <int> newv(v);
      for(int i = lst + 1; i <= n; i += 2) {
        newv.push_back(i);
        generate(newv, k, n, T / 2);
        newv.pop_back();
      }
    });
    vector <int> aux(v);
    for(int i = lst + 2; i <= n; i += 2) {
      aux.push_back(i);
      generate(aux, k, n, T - T / 2);
      aux.pop_back();
    }
    t.join();
  }
}

int main() {
  generate(vector <int> (), 3, 5, 2);
  cout << cnt << '\n';
}
