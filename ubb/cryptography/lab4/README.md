# Lab4 - Factorizing

## Classic algorithm
The classic algorithm is pretty straight forward:
- We take each possible divisor, and when we find one, we keep dividing that number
with the same divisor while we can. We also only need to go only until `sqrt(n)`.

A simple pseudocode for this is:
```python
def factorize(n):
  factors = []                  # will keep our result
  for p from 2 to sqrt(n):      # iterate from 2 to sqrt(n)
    cnt = 0                     # will store the current power of the current prime
    while n % p == 0:           # while we can,
      n /= p                    # divide n by p
      cnt += 1                  # increase the count
    if cnt != 0:                # if it was a divisor
      factors.append((p, cnt))  # append to the solution
  if n != 1:                    # there may be only one divisor left
    factors.append((n, 1))      # append if necessary
  return factors                # return the result

```
Other approches precomputes all the primes in the interval [2, sqrt(n)], and the implementation
would be faster so that you are not iterating to all numbers in the interval, but rather on only
the number of divisors there. However, a precomputation is neccesary.

| Number | Algorithm | Processor cycles | Time (milliseconds) |
|--------|-----------|------------------|---------------------|
| `48` | CLASSIC ALGORITHM  | `257` | `0.257` |
| `48` | POLLARD RHO  | `125` | `0.125` |
| `59290505918` | CLASSIC ALGORITHM  | `159` | `0.159` |
| `59290505918` | POLLARD RHO  | `128` | `0.128` |
| `270` | CLASSIC ALGORITHM  | `125` | `0.125` |
| `270` | POLLARD RHO  | `135` | `0.135` |
| `8266` | CLASSIC ALGORITHM  | `148` | `0.148` |
| `8266` | POLLARD RHO  | `121` | `0.121` |
| `38345` | CLASSIC ALGORITHM  | `128` | `0.128` |
| `38345` | POLLARD RHO  | `137` | `0.137` |
| `571445` | CLASSIC ALGORITHM  | `126` | `0.126` |
| `571445` | POLLARD RHO  | `124` | `0.124` |
| `8561193` | CLASSIC ALGORITHM  | `208` | `0.208` |
| `8561193` | POLLARD RHO  | `121` | `0.121` |
| `94786230` | CLASSIC ALGORITHM  | `127` | `0.127` |
| `94786230` | POLLARD RHO  | `123` | `0.123` |
| `328186067` | CLASSIC ALGORITHM  | `151` | `0.151` |
| `328186067` | POLLARD RHO  | `129` | `0.129` |
| `4836989149` | CLASSIC ALGORITHM  | `168` | `0.168` |
| `4836989149` | POLLARD RHO  | `4005` | `4.005` |



## Pollard p algorithm
The algorithm returns a non-obvious divisor of a number. It uses Floyd's idea of detecting cycles,
also knonw as the rabbit & turtle problem.

### Pseudocode

```
    x ← 2; y ← 2; d ← 1
    while d = 1:
        x ← g(x)
        y ← g(g(y))
        d ← gcd(|x - y|, n)
    if d = n:
        return failure
    else:
        return d
```
