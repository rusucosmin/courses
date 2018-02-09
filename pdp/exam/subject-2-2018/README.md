# Exam to Parallel and Distributed Programming `feb 2018, subject no 2`

1. (3p) Write a parallel (distributed or local, at your choice) that computes the discrete
convultion of a vector with another vector. The convolution is defined as:
`r(i) = sum(a(i) * b(i - j), j = 0..n)`

2. (3p) Consider the following code for enqueueing a continuation on a future. Identify and fix
the thread-safety issue.

```cpp
template<typename T>
class Future {
  list<function<void(T)>> continuations;
  T val;
  bool has_value;
public:
  Future(): has_value(false) {}
  void set(T v) {
    val = v;
    hasValue = true;

    for(function<void(T)>& f: continuations) {
      f(v);
    }

    continuations.clear();
  }
  void addContinuation(function<void(T)> f) {
    if(hasValue) {
      f(val);
    } else {
      continuations.push_back(f);
    }
  }
}
```

3. (3p) Write a parallel algorithm that computes the product of 2 matrices.
