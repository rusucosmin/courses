# Solution for the `subject-1-2017`

## 1. (3.5p) Write a parallel (distributed or local, at your choice) program for finding a Hamiltonian path starting at a given vertex.

That is, you are given a graph with n vertices
and must find a path that starts at vertex 0 and goes through each of the other vertices
exactly once. Find a solution, if one exits. If needed, assume you have a function that gets
a vector containing a permutation of length n and verifies if it is Hamiltonian path in the
given graph or not.

See `hamilton.cpp`


## 2. (2.5p) Consider the following code for transferring money from one account to another.

You are required to write a function parsing all accounts (assume you
have a `vector <Account>`) and compute the total amount of money there, so that
it doesn't interfere with possible transfers at the same time. Change the
transfer function if needed, but it must be able to be called concurrently
for independent pair of accounts.

```cpp
struct Account {
    unsigned id;
    unsigned balance;
    mutex mtx;
};

bool transfer(Account& from, Account& to, unsigned amount) {
  {
    unique_lock<mutex> lck1(from.mtx);
    if(from.balance < amount) return false
    from.balance -= amount;
  }
  {
    unique_lock<mutex> lck2(to.mtx);
    to.balance += amount;
  }
}
```

### Concurrentcy issue

There is a problem with this method if we want to compute the sum,
because it may be the case that the amount is taken out of an account,
but not yet added to the other one, such that some amount is lost from
the entire sum.

### Solution

Lock the two nodes simulateously

### Code
```cpp
bool transfer(Account& from, Account& to, unsigned amount) {
  unique_lock<mutex> lck1(from.mtx);
  unique_lock<mutex> lck2(to.mtx);
  if(from.balance < amount) return false
  from.balance -= amount;
  to.balance += amount;
  return true;
}

int getSum(vector <Account> v) {
  int sum = 0;
  for(auto account : v) {
    account.mtx.lock();
    sum += account.balance;
  }
  for(auto account : v) {
    account.mtx.unlock();
  }
  return sum;
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














