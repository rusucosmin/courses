# README
[![Build Status](https://travis-ci.org/rusucosmin/cryptography.svg?branch=master)](https://travis-ci.org/rusucosmin/cryptography)

Public Key Cryptography course assignments

Ruby version: 2.5.2
Rails version: 5.1.4

# Documentation
## Laboratory 1 - Affine cipher
* The affine cipher is a type of monoalphabetic substitution cipher, wherein
  each letter in an alphabet is mapped to its numeric equivalent, encrypted using
  a simple mathematical function, and converted back to a letter. The formula used
  means that each letter encrypts to one other letter, and back again, meaning the
  cipher is essentially a standard substitution cipher with a rule governing which
  letter goes to which. As such, it has the weaknesses of all substitution
  ciphers. Each letter is enciphered with the function `(ax + b) mod 26`,
  where `b` is the magnitude of the shift.
* A particular example of the affine cipher is the caesar cipher (with `a = 1`
  and `b = 1`).
* The encryption function is `E(x) = (a * x + b) mod m`
* The decryption function is `D(x) = invMod(a) * (x - b) mod m`
* Where `(a, b)` is the key of the affine cipher
* `m` is the length of the alphabet
* `gcd(a, m) == 1`

# Run locally

In order to run this project:
* clone it using
`git clone https://github.com/rusucosmin/cryptography`
* navigate to the project
`cd cryptography`
* run the local instance
`rails server`
