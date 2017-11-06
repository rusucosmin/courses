Finite automata
===============


File content description
------------------------

* The file that describes the finite automata is a **JSON object**
* The JSON object **must** contain:
  1. field **`"states"`**
      - containing an array of **states**
      - states can be everything from **strings** to **integers** or other **hashable** objects
  2. field **`"alphabet"`**
      - can contain both a string containing all the letters from the alphabet (duplicates can exist,
    and we will automatically remove them)
      - can contain an array of "letters" which can be either characters or strings
  3. field **`"transitions"`**
      - an array of "transition" object containing:
          - **`"from"`** field: a valid state from which we came from
          - **`"letter"`** field: a valid a letter from the alphabet, or an array containing valid letters
          - **`"to"`** field: the state we will move if we follow the arrow corresponding to letter
  4. field **`"initial_state"`**
      - the initial state of the finite automata
  5. field **`"accepted_states"`**
      - an array of all the accepted states
* Example
```javascript
{
  "states": ["q0", "q1", "q2"],
  "alphabet": "abcfeghijklmnopqrstuvwxyz",
  "transitions": [{
      "from": "q0",
      "to": "q1",
      "letter": "a"
    }, {
      "from": "q1",
      "to": "q2",
      "letter": ["a"]
    }
  ],
  "initial_state": "q0",
  "accepted_states": ["q2"]
}
```

[C++ Integer Literal](http://en.cppreference.com/w/cpp/language/integer_literal)
---------------------

An integer literal is a primary expression of the form
* decimal-literal integer-suffix(optional)  (1)
* octal-literal integer-suffix(optional)  (2)
* hex-literal integer-suffix(optional)  (3)
* binary-literal integer-suffix(optional) (4) (since C++14)

