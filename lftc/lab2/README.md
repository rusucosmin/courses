Finite automata
===============


File content description
------------------------

- The file that describes the finite automata is a JSON object
- The JSON object should contain:
  1. field `"states"`
    - containing an array of **states**
    - states can be everything from **strings** to **integers** or other **hashable** objects
  2. field `"alphabet"`
    - can contain both a string containing all the letters from the alphabet (duplicates can exist,
    and we will automatically remove them)
    - can contain an array of "letters" which can be either characters or strings
  3. field `"transitions"`
    - an array of "transition" object containing:
       - `"from"` field: a valid state from which we came from
       - `"letter"` field: a valid a letter from the alphabet
       - `"to"` field: the state we will move if we follow the arrow corresponding to letter
  4. field `"initial\_state"`
    - the initial state of the finite automata
  5. field `"accepted\_states"`
    - an array of all the accepted states
