# Public Key Cryptography - Lab2

- The library for big number is loaded from
  [here](https://sites.google.com/site/indy256/algo_cpp/bigint)

- Implemented the following three algorithms:
  - Finding the greatest common divisor by substracting the minimum from the other one.
  - Euclid algorithm which is basically based on the proof that `gcd(a, b) = gcd(b, a % b)`
  - Factorization algorithm where we factorise each number and take the common primes at the least
    power

- Every operation is done on the bigint class which implements all the basic arithmetic for big
  integers, such as addition by big/small, subtraction by a big/small, division, modulo.

- The runtime analysis was done in a python jupyter notebook based on the data that was spit by the
  `c++` program.
