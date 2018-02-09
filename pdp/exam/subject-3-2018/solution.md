# Exam to Parallel and Distributed Programming `feb 2018, subject no 3`

## 1. (3p) Write a parallel or distributed program that counts the number of subsets of `k` out of `N` that satisfy a given property.

You have a function (`bool pred(vector <int> const& v)`) that
verifies if a given subset satisfies the property. Your program shall call that function once for
each subset of `k` elements and count the number of times it returns true.

see: `comb_async.cpp`

## 2. (3p) Consider the following code for enqueueing a work item to a thread pool.

Find the concurrency issue and fix it. Also, add a mecahnism to end the threads at shutdown.

```cpp
class ThreadPool {
  condition_variable cv;
  mutex mtx;
  list<function<void()>> work;
  vector <thread> threads;

  void run() {
    while(true) {
      if(work.empty()) {
        unique_lock<mutex> lck(mtx);
        cv.wait(lck);
      } else {
        function<void()> wi = work.front();
        work.pop_front();
        wi();
      }
    }
  }
public:
  explicit ThreadPool(int n) {
    threads.resize(n);
    for(int i = 0; i < n; ++ i) {
      threads.emplace_back([this](){run();});
    }
  }
  void enqueue(function <void()> f) {
    unique_lock<mutex> lck(mtx);
    work.push_back(f);
    cv.notify_one();
  }
}
```

### Concureency issue

The issue here is that the ThreadPool is started with `n = 2` and on the main thread, we create
another two threads that calles the `enqueue()` method, both will try to access `work.front()`
element, and follow with an `work.pop_front()`.

### Solution

The critical resource is the list. The correct way would be to have the mutex to also lock the
other branch of the is case

### Code

```cpp
  void run() {
    while(true) {
      if(work.empty()) {
        unique_lock<mutex> lck(mtx);
        cv.wait(lck);
      } else {
        {
          unique_lock<mutex> lck(mtx);
          function<void()> wi = work.front();
          work.pop_front();
        }
        wi();
      }
    }
  }
```


## 3. (3p) Write a parallel algorithm that computes the product of two big numbers.

see: `product.cpp`


