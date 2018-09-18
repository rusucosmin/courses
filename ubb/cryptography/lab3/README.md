# Public Key Cryptography

Assigned task: 2. Implement the algorithm for solving systems of congruences.

# Systems of Linear Congruences


## General system of simulatenous linear congruences

```
a_1 * x ≡ b_1 (mod n_1)
a_2 * x ≡ b_2 (mod n_2)
...
a_k * x ≡ b_k (mod n_k)
```


## Simplified general system of simulatenous linear congruences
This general equation can be simplified by dividing each congruence through by
`(a_i, n_i)`, then multiplying by the inverse mod `mi = n_i / (a_i, n_i)`.
The simplified system may or may not be solvable, but in any case, it must have
the same set of solutions as the original system

```
x ≡ c_1 (mod m_1)
x ≡ c_2 (mod m_2)
...
x ≡ c_k (mod m_k)
```

## Chinese Remainder Theorem
Let `m_1, m_2, ..., m_k` be *pairwise* relatively prime moduli. Then the above
system of congruences has a unique solution modulo the product `m = m_1 * m_2 * ... * m_k`.

## Theorem
The above system of linear congruences has a solution iff for all `i ≠ j`,
`c_i ≡ c_j (mod (m_i,m_j)).`
The solution, if it exists, is unique `mod m = m_1 * m_2 * ... * m_k`.

## Bibliography
1. [Theorems & Proofs](http://www.cs.xu.edu/math/math302/08f/06_CRT.pdf)
