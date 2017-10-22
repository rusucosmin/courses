/*
  3. Summation with fixed structure of inputs

  We have to keep the values of some integer variables. Some of them are primary variables; they represent input data. The others are secondary variables, and represent aggregations of some other variables. In our case, each secondary variable is a sum of some input variables. The inputs may be primary or secondary variables. However, we assume that the relations do not form cycles.

  At runtime, we get notifications of value changes for the primary variable. Processing a notification must atomically update the primary variable, as well as any secondary variable depending, directly or indirectly, on it. The updating shall not re-compute the sums; instead, you must use the difference between the old value and the new value of the primary variable.

  From time to time, as well as at the end, a consistency check shall be performed. It shall verify that all the secondary variables are indeed the sums of their inputs, as specified.
*/


#include <iostream>
#include <chrono>
#include <fstream>
#include <vector>
#include <map>
#include <stdlib.h>
#include <time.h>
#include <thread>
#include <mutex>

using namespace std;

#define NODE_MUTEX
//#define ENABLE_GLOBAL_MUTEX

class Node {
protected:
  #ifdef NODE_MUTEX
  std::mutex node_mtx;
  #endif
public:
  virtual int getIndex() = 0;
  virtual int getValue() = 0;         // thread safe
  virtual void addToValue(int) = 0;   // thread safe
  virtual int computeValue() = 0;
};

class BaseNode : public Node {
protected:
  int value, index;
public:
  BaseNode(int ind) {
    index = ind;
    value = 0;
  }
  BaseNode(int ind, int x) {
    index = ind;
    value = x;
  }
  virtual int getIndex() {
    return index;
  }
  virtual int getValue() {
    #ifdef NODE_MUTEX
    node_mtx.lock();
    #endif
    int auxval = value;
    #ifdef NODE_MUTEX
    node_mtx.unlock();
    #endif
    return auxval;
  }
  virtual void addToValue(int x) {
    #ifdef NODE_MUTEX
    node_mtx.lock();
    #endif
    value += x;
    #ifdef NODE_MUTEX
    node_mtx.unlock();
    #endif
  }
  virtual int computeValue() {
    return value;
  }
};

class InternalNode : public BaseNode {
private:
  vector <Node*> dependency;
public:
  InternalNode(int ind) : BaseNode(ind) {
  }
  void addDependency(Node *n) {
    dependency.push_back(n);
  }
  virtual int computeValue() {
    value = 0;
    for(auto it : dependency) {
      value += it->computeValue();
    }
    return value;
  }
};


class ComputationalGraph {
private:
  #ifdef ENABLE_GLOBAL_MUTEX
  mutex global_mutex;
  #endif
  map<int, Node*> nodes;
  map<Node*, vector<Node*>> dependants;
  int n, m;
  void dfs(Node *node, int quantity) {
    node->addToValue(quantity);
    for(auto it : dependants[node]) {
      dfs(it, quantity);
    }
  }
public:
  void updateBaseNode(BaseNode* baseNode, int newValue) {
    #ifdef ENABLE_GLOBAL_MUTEX
    global_mutex.lock();
    #endif
    dfs(baseNode, newValue - baseNode->getValue());
    #ifdef ENABLE_GLOBAL_MUTEX
    global_mutex.unlock();
    #endif
  }
  void loadGraph(string filename) {
    ifstream fin(filename);
    fin >> n; // number of leaf nodes
    for(int i = 1; i <= n; ++ i) {
      int x;
      fin >> x;
      Node *node = new BaseNode(i, x);
      nodes[i] = node;
    }
    fin >> m; // number of dependencies
    for(int i = 1; i <= m; ++ i) {
      int x, y; // y depends on x
      fin >> x >> y;
      if (!nodes[x]) {
        nodes[x] = new InternalNode(x);
      }
      if (!nodes[y]) {
        nodes[y] = new InternalNode(y);
      }
      dynamic_cast<InternalNode*>(nodes[y])->addDependency(nodes[x]);
      dependants[nodes[x]].push_back(nodes[y]);
    }
  }
  void computeInitialValue() {
    for(auto it : nodes) {
      it.second->computeValue();
    }
  }
  void printValues() {
    for (auto it : nodes) {
      cout << "value of " << it.first << " is: " << it.second->getValue() << '\n';
    }
  }
  BaseNode* getRandomBaseNode() {
    return dynamic_cast<BaseNode*>(nodes[rand() % n + 1]);
  }
};

int T = 1000;

int getRandomInteger(int _max, int _min) {
  return _min + (rand() % static_cast<int>(_max - _min + 1));
}

int main() {
  auto start = std::chrono::high_resolution_clock::now();
  srand(time(NULL));
  vector <thread> threads;
  ComputationalGraph g;
  g.loadGraph("graph.in");
  g.computeInitialValue();
  for(int t = 0; t < T; ++ t) {
    BaseNode* currentNode = g.getRandomBaseNode();
    int newVal = getRandomInteger(-10, 10);
    cerr << "thread " << t + 1 << " updates node " << currentNode->getIndex()
        << " with " << newVal << '\n';
    threads.push_back(thread(&ComputationalGraph::updateBaseNode, &g, currentNode, newVal));
  }
  for(int t = 0; t < T; ++ t) {
    threads[t].join();
  }
  g.printValues();
  auto finish = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> elapsed = finish - start;
  cerr << "Elapsed time: " << elapsed.count() << '\n';
  return 0;
}
