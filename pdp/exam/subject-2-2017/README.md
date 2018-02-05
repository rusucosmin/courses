# Exam to Parallel and Distributed Programming `jan-feb 2017, subject no. 1`

1. (3.5p) Write a parallel (distributed or local, at your choice) program for finding a
Hamiltonian path starting at a given vertex. That is, you are given a graph with n vertices
and must find a path that starts at vertex 0 and goes through each of the other vertices
exactly once. Find a solution, if one exits. If needed, assume you have a function that gets
a vector containing a permutation of length n and verifies if it is Hamiltonian path in the
given graph or not.

2. (2.5p) Consider the following code for transferring money from one account to
another. You are required to write a function parsing all accounts (assume you
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


3. (3p) We have n servers that can communicate to each other. There are events producing on each of
them; each event has an associated information. Each server must write a history of all events
(server and event info) produced on all servers, and, furthermore, the recorded history must be the
same for all servers. Write a distributed algorithm that accomplishes that. Consider the case n = 2
for starting.

