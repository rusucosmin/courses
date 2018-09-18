#include <mutex>
#include <condition_variable>
#include <thread>
#include <iostream>
#include <fstream>
#include <queue>
#include <tuple>
#include <chrono>
#include <string>

using namespace std;
using namespace std::chrono;

const string data[] = {"mult0.in", "mult1.in", "mult2.in", "mult3.in",
    "mult4.in", "mult5.in", "mult6.in"};
const int T[] = {1, 3, 5, 10, 25, 50, 100};
const int maxn = 1005;

//#define debug

mutex mx;
//mutex mx_mat[maxn][maxn];
condition_variable cv;
queue <tuple<int, int, int>> q;

int n, a[maxn][maxn], b[maxn][maxn], c[maxn][maxn], rez[maxn][maxn];
bool finished;

ofstream logger(to_string(duration_cast<milliseconds>(
    system_clock::now().time_since_epoch()).count()) + ".log");

inline void loadData(string name) {
  ifstream fin(name);
  fin >> n;
  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < n; ++ j) {
      fin >> a[i][j];
    }
  }
  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < n; ++ j) {
      fin >> b[i][j];
    }
  }
  for(int i = 0; i < n; ++ i) {
    for(int j = 0; j < n; ++ j) {
      fin >> c[i][j];
    }
  }
  #ifdef debug
  cerr << "data loaded\n";
  #endif
}

inline void producer(int line, int T) {
  for(int i = line; i < n; i += T) {
    for(int j = 0; j < n; ++ j) {
      int aux_i_j = 0;
      for(int k = 0; k < n; ++ k) {
        aux_i_j += a[i][k] * b[k][j];
      }
      {
        lock_guard<mutex> lk(mx);
        // produce (i, j, aux_i_j)
        #ifdef debug
        cerr << "producing (" << i << ", " << j << ", " << aux_i_j << ")\n";
        #endif
        q.push(make_tuple(i, j, aux_i_j));
      }
      cv.notify_all();
    }
  }
}

inline void consumer(int tid, int T) {
  while(true) {
    unique_lock<mutex> lk(mx);
    cv.wait(lk, []{return finished || !q.empty(); });
    if (finished)
      break;
      tuple<int, int, int> el = q.front();
      q.pop();
      //lk.unlock();
      int i = get<0>(el);
      int j = get<1>(el);
      int x = get<2>(el);
      #ifdef debug
      cerr << tid << " consuming (" << i << ", " << j << ", " << x << ")";
      #endif
      for(int k = 0; k < n; ++ k) {
 //       lock_guard<mutex> lck(mx_mat[i][k]);
        rez[i][k] += x * c[j][k];
      }
  }
}

int main() {
  logger << "size,number_of_threads,duration\n";
  for(int di = 0; di < 7; ++ di) {
    loadData(data[di]);
    for(int tj = 0; tj < 7; ++ tj) {
      cerr << "test " << di << ' ' << n << " " << T[tj] << '\n';
      int t = T[tj];
      auto start = high_resolution_clock::now();
      vector <thread> producers, consumers;
      for(int i = 0; i < min(n, t); ++ i) {
        producers.push_back(thread(producer, i, t));
      }
      for(int i = 0; i < min(n, t); ++ i) {
        consumers.push_back(thread(consumer, i, t));
      }
      for(int i = 0; i < producers.size(); ++ i) {
        producers[i].join();
      }
      {
        lock_guard<mutex> lk(mx);
        finished = true;
      }
      cv.notify_all();
      for(int i = 0; i < consumers.size(); ++ i) {
        consumers[i].join();
      }
      #ifdef debug
      cerr << '\n';
      for(int i = 0; i < n; ++ i) {
        for(int j = 0; j < n; ++ j) {
          cerr << rez[i][j] << ' ';
        }
        cerr << '\n';
      }
      #endif
      auto finish = high_resolution_clock::now();
      auto total = finish - start;
      logger << n << "," << t << "," << duration_cast<milliseconds>(total).count() << "\n";
    }
  }
}
