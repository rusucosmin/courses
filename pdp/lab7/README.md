#Requirements

Solve both problems below:

1. Given a sequence of `n` numbers, compute the sums of the first `k` numbers,
for each `k` between `1` and `n`. Parallelize the computations, to optimize for
low latency on a large number of processors. Use at most `2*n` additions, but
no more than `2*log(n)` additions on each computation path from inputs to an
output.

Example: if the input sequence is `1 5 2 4`, then the output should be `1 6 8 12`.

2. Add `n` big numbers. We want the result to be obtained digit by digit,
starting with the least significant one, and as soon as possible. For this
reason, you should use `n-1` threads, each adding two numbers. Each thread should
pass the result to the next thread. Arrange the threads in a *binary tree*. Each
thread should pass the sum to the next thread through a queue, digit by digit.


#Documentation

I solved the two problems using `C++`.
The performance is measured on my personal computer with the following config:
```
MacBook Pro (13-inch, 2017)
Processor: 2.3 GHz Intel Core i5
Memory: 16 GB 2133 MHZ LPDDR3
Graphics: Intel Iris Plus GRaphics 640 1536 MB
```

##Algorithms

###Partial Sums

I used dynamic programming to solve this problem. Each thread can compute the
sum of every subsequence of the array (not neccessarry starting on the first
position).
Let's denote `a` - the initial array and let the following discriminant:
```
dp[k][i] = sum(a[j]) where i <= j <= i + 2^k - 1
It follows that
dp[0][i] = a[i]
dp[k][i] = dp[k - 1][i] + dp[k - 1][i - 2^(k - 1)]
```
Having this table precomputed, it's easy to compute the sum of the first k
elements. Just start at position 0 and break the interval in other `log(k)`
intervals of size a power of two.

Let `T` be the number of threads.
Thread number `i where 0 <= i < T` will compute every partial sum `k` such that
`k mod T = i`.

Source code: `sums.cpp`

###Addition of n numbers

The requirements were very clear. So we arranged the threads in a binary tree,
such that the 'root' thread computes the final sum and the leaf nodes
takes as input two initial numbers, compute their sum digit by digit and
sends the result to the parent thread.
The threads used a syncronized queue to send the digits.

Source code: `add.cpp`

##Synchronization

###Partial Sums

No synchornization is needed because everything is independent in terms of
what variables they modify (the threads write to indepdent variables and
and read read-only variables).

###Addition of n numbers

The only synchronization mechanism we need is a Threadsafe-Queue.
In this context we mean that the queue should support at least:
`enqueue(elem)` - adds an element to the queue
`dequeue()`     - returnes the head of the queue and in case it's empty
                - block the calling threads until an element is available.
This two methods are implemented in `safequeue.h` using a `mutex`, a normal
`queue` and a `condition_variable`.

##Performance measurements

Both program will tell you the number of clock cycles it took and the number of
seconds.

###Partial Sums

The program will tell you the number of clock cycles it took and the number of
seconds.

###Addition of n numbers

Run `eval.sh` to test the program for correctness and to see the times for each
test case. My computer is limited on the number of threads I can spawn per
process, so adding `a lot` of number usullay throws an error.

