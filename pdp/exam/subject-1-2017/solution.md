# Solution for the `subject-1-2017`

## 1. (3.5p) Write a parallel (distributed or local, at your choice) program for solving the k-coloring problem

That is, you are given a number k, and n objects and some pairs among them that have
distinct colors. Find a solution to color them with at most n colors in total, if one exists.
Assume you have a function that gets a vector with n integers representing the assignment of colors
to objects and checks if the constraits are obeyed or not.

### Solution

We will map every possible coloring to a number in base `k`, so the numnber `0` represents the colouring
`000...000`. We have number in the interval [0, k^n - 1].

Now, each thread `i` will check all the numbers x such that `x % t == i`.

### Code

```cpp

bool check(vector <int> colour);

vector <int> to_color(int sol, int n, int k) {
  vector <int> v;
  for(int i = 0; i < n; ++ i) {
    v.push_back(sol % k);
    sol /= k;
  }
  return v;
}

vector <int> solve(int n, int k, int T) {
  int maxi = 1;
  for(int i = 0; i < n; ++ i) {
    maxi *= k;
  }
  vector <int> sol;
  vector <thread> threads;
  for(int t = 0; i < T; ++ t) {
    threads.push_back([&sol, i, n, k](){
      for(int j = i; j < maxi && sol.size() == 0; j += T) {
        vector <int> col = to_color(sol);
        if(check(col, n, k) {
          sol = col;
        }
      }
    });
  }
  for(int i = 0; i < T; ++ i) {
    threads[i].join();
  }
  return sol;
}
```

## 2. (2.5p) Consider the following code for inserting a new value into a linked list at a given position

We assume that insertions can be called concurrently, but not for the same position.
Find and fix the concurrency issue. Also, describe a function for parsing the linked list.

```cpp
struct Node {
    unsigned payload;
    Node* next;
    Node* prev;
    mutex mtx;
};

void insertAfter(Node* before, unsigned value) {
    Node* node = new Node;
    node->payload = value;
    Node* after = before->next;
    before->mtx.lock();
    before->next = node;
    before->mtx.unlock();
    after->mtx.lock();
    after->prev = node;
    after->mtx.unlock();
    node->prev = before;
    node->next = after;
}
```

### Concurrentcy issue
Here is an example that illustrates a concurrency issue:

```
// the list A -> B
thread1:
  insertAfter(nodeA, x);
thread2:
  insertAfter(nodeA->next, y);
```

It could happend that after these possible solutions:

We would accept the following two cases:
```
A -> x -> y -> B
A -> x -> B -> y
```

However, this could happen this:

`nodeA->x->B`


### Solution

Lock the two nodes simulateously

### Code
```cpp
void insertAfter(Node* before, unsigned value) {
    Node* node = new Node;
    node->payload = value;
    Node* after = before->next;
    before->mtx.lock();
    after->mtx.lock();
    before->next = node;
    after->prev = node;
    before->mtx.unlock();
    after->mtx.unlock();
    node->prev = before;
    node->next = after;
}
```

## 3. (3p) We have n servers that can communicate to each other.

There are events producing on each of them; each event has an associated information. Each server must write a history of all events
(server and event info) produced on all servers, and, furthermore, the recorded history must be the
same for all servers. Write a distributed algorithm that accomplishes that. Consider the case n = 2
for starting.


### Solution
Let's consider the case when `n = 2`. Let's name the processes `A` and `B`.


Every process will keep a `Lamport clock` and pass that on each message.

Suppose an event occurs in the process `A`. Then, process `A` will increate it's timestamp `t` by one,
and send that event alongside `t` at the process `B` - this is called `PREPARE` event. Process `B` computes the maximum between
its internal clock and the timestamp of the message and adds one. It send back an `OK` with that
computed timestamp. Process `A` receives the `OK` and sends back a `COMMIT` message. They both
agreed on this value.

The generalization to `n > 2` follows easily.

Each process having an occuring event will:
* broadcast `PREPARE` with the timestamp
* waits for `OKs` from all the other processes
* computes the maximum amongs the `OKs` timestamps
* broadcast `COMMIT` to each process


There is only one little problem. A process may have previously gave an `OK` but did not get any `COMMIT`
yet for that event. So, in case another `COMMIT` appears, it can't write that to a file because the `COMMIT`
from the previously sent `OK` may be either before, or after the current `COMMIT`. That's why,
each process will maintain a list of given `OKs` as well as a list of `COMMITs` to be flushed to disk.

Note. Every tie can be solved by chosing an initial *arbitrary* ordering of the processes. Such as the `PID`
or `IP` if they live on different hosts.














