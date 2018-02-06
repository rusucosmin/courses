#include <iostream>
#include <thread>
#include <vector>
#include <atomic>

using namespace std;

bool check(vector <int> v) {
  if(v[0] % 2 == 0) {
    return true;
  }
  return false;
}

bool contains(vector <int> v, int n) {
  for(auto it : v) {
    if(it == n) {
      return true;
    }
  }
  return false;
}

atomic <int> cnt;

void back(vector <int> sol, int T, int n) {
  if(sol.size() == n) {
    if(check(sol)) {
      cnt ++;
    }
    return;
  }
  if(T == 1) {
    for (int i = 1; i <= n; ++ i) {
      if(contains(sol, i)) continue;
      sol.push_back(i);
      back(sol, T, n);
      sol.pop_back();
    }
  } else {
    vector <int> x(sol);
    thread t([&](){
      for(int i = 1; i <= n; i += 2) {
        if(contains(x, i)) continue;
        x.push_back(i);
        back(x, T / 2, n);
        x.pop_back();
      }
    });
    for(int i = 2; i <= n; i += 2) {
      if(contains(sol, i)) continue;
      sol.push_back(i);
      back(sol, T - T / 2, n);
      sol.pop_back();
    }
    t.join();
  }
}

int main() {
  back(vector <int>(), 2, 3);
  cout << cnt.load() << '\n';
}
