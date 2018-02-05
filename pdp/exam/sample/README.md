# Sample exam subject

1. Write a parallellized and distributed version of the QuickSort algorithm using MPI.

2. Consider the following code. Find and fix the concurrency issue.

```cpp
struct Account {
    unsigned id;
    unsigned balance;
    mutex mtx;
};

bool transfer(Account& from, Account& to, unsigned amount) {
    unique_lock lck1(from.mtx);
    unique_lock lck2(to.mtx);
    if(from.balance < amount) return false;
    from.balance -= amount;
    to.balance += amount;
}
```

3. Give an algorithm for solving the following variant of the consensus problem:

Each process i has an input value vi;
All processes must decide some output value; the output value must be the same for all processes and, if all inputs are equal, then the common output must be equal to that input;
We have synchronous rounds;
The processes are all correct;
Messages may be lost; however, if a party sends infinitely many messages, then infinitely many will be delivered;
Each process must decide after a finite amount of time; however, it can continue the algorithm forever.

