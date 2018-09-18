#include <iostream>
#include <fstream>
#include "safequeue.h"
#include <thread>

using namespace std;

inline void doIt(int st, int dr, vector <string>& nums, SafeQueue<char> &q) {
  if(st == dr) {
    for(int i = 0; i < nums[st].size(); ++ i) {
      q.enqueue(nums[st][i]);
    }
    q.enqueue('\0');
    return ;
  }
  int mid = (st + dr) / 2;
  SafeQueue<char> q1;
  thread t1([st, mid, &nums, &q1](){doIt(st, mid, nums, q1);});
//  doIt(st, mid, nums, q1);
  SafeQueue<char> q2;
  thread t2([mid, dr, &nums, &q2](){doIt(mid + 1, dr, nums, q2);});
//  doIt(mid + 1, dr, nums, q2);
  bool firstStopped = 0;
  bool secondStopped = 0;
  char T = 0;
  while(true) {
    char res = T;
    T = 0;
    if(!firstStopped) {
      char e1 = q1.dequeue();
      if(e1 == 0) {
        firstStopped = true;
      } else {
        res += e1 - '0';
      }
    }
    if(!secondStopped) {
      char e2 = q2.dequeue();
      if(e2 == 0) {
        secondStopped = true;
      } else {
        res += e2 - '0';
      }
    }
    if(firstStopped && secondStopped) {
      if(res > 0) {
        q.enqueue(res + '0');
      }
      break;
    }
    if(res > 9) {
      res -= 10;
      T = 1;
    }
    q.enqueue(res + '0');
  }
  q.enqueue('\0');
  t1.join();
  t2.join();
}

int main() {
  clock_t t;
  t = clock();

  ifstream fin("add.in");

  int n;
  fin >> n;

  vector <string> nums;

  for(int i = 0; i < n; ++ i) {
    string x;
    fin >> x;
    reverse(x.begin(), x.end());
    nums.push_back(x);
  }

  SafeQueue<char> q;
  doIt(0, nums.size() - 1, nums, q);
  string sol = "";
  while(true) {
    char e1 = q.dequeue();
    if(!e1) {
      break;
    }
    sol += e1;
  }

  reverse(sol.begin(), sol.end());

  ofstream fout("add.out");

  fout << sol << '\n';

  t = clock() - t;
  cout << "Addition of " << n << " numbers took me "  << t
      << " cycles (" << static_cast<float> (t) / CLOCKS_PER_SEC << " seconds)\n";
}
