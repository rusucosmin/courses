# Solution for the `Sample exam subject - 2018`

## 1. Write a parallellized and distributed version of the QuickSort algorithm using MPI.

See `quicksort-mpi.cpp`

## 2. Consider the following code. Find and fix the concurrency issue.

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

### Concurrency issue
There is a potential deadlock in this situation if there are two transfers happending at the same time like this:

```
thread1:
  transfer(account_a, account_b, x)
thread2:
  transfer(account_b, account_a, y)
```

If the two threads can acquire the first lock thei need (the first unique_lock from the method), a deadlock will happen.

### Solution
Assuming the ids are unique (obviously), lock the accounts in order.


### Code

```cpp
bool transfer(Account& from, Account& to, unsigned amount) {
    if(from.id < to.id) {
      unique_lock lck1(from.mtx);
      unique_lock lck2(to.mtx);
    } else if (from.id > to.id) {
      unique_lock lck1(to.mtx);
      unique_lock lck2(from.mtx);
    } else {
      // tranfer from the same account
      if(from.balance < amount) return false;
      return true;
    }
    if(from.balance < amount) return false;
    from.balance -= amount;
    to.balance += amount;
    return true;
}
```

## 3. Give an algorithm for solving the following variant of the consensus problem:

* Each process i has an input value vi;
* All processes must decide some output value; the output value must be the same for all processes and, if all inputs are equal, then the common output must be equal to that input;
* We have synchronous rounds;
* The processes are all correct;
* Messages may be lost; however, if a party sends infinitely many messages, then infinitely many will be delivered;
* Each process must decide after a finite amount of time; however, it can continue the algorithm forever.

### Solution

Since no process is faulty, it is enough to make the first process send its value to all other processes and have all processes agree on that value. There is no risk that the first process sends distinct values to distinct processes; however, we must make sure that the value sent by the first process arrives at all other processes.

So, the solution is the following:

process 1 decides y1=x1; Then, forever, it waits for requests from other processes and answer each request by sending back x1 to the requester.
each of the other processes repeatedly sends requests to process 1 until it receives an answer. At that moment, it decides the values read from that answer.
