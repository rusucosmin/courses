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

Lexer using the implemented finite automata
-------------------------------------------

We will change the lexer from the `laboratory 1` to use the finite automatas for
detecting identifiers, symbols and constants.

The lexer will have three finite automatas:
* `symbols_fa` -> the finite automata that accepts all the symbols of our language
* `identifiers_fa` -> the finite automata that accepts all the possible identifiers of our language
* `constants_fs` -> the finite automata that accepts all the possible constants of our language

Algorithm
---------
```bash
For each line in the source code program:
  while line is not empty:
    strip the line (remove trailing whitespace characters)
    _sym = symbols_fa.longest_accepted_prefix(line)
    _id = identifiers_fa.longest_accepted_prefix(line)
    _const = const_fa.longest_accepted_prefix(line)
    if _sym == _id:
      _id = ""
    # now, exactly one of the three variables will be non-empty
    # we will find that one and remove it from current line
    # then repeat
    if _id is non-empty:
      found_identifier(_id)
      line = line - _id
    elif _sym is non-empty:
      found_symbol(_sym)
      line = line - _sym
    elif _const is non-empty:
      found_const(_const)
      line = line - _const
```

