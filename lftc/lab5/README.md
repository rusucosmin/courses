# SLR Parser
 SLR parsing method

The assignment is divided in the following phases:
* STEP 1: perform the parsing of an input sequence
  - Input
    - a context free grammar (the example from course)
    - an input sequence
  - Output: the parsing tree corresponding to the input sequence
  or a message in case the sequence is not accepted.
* STEP 2: parsing
  - Input: PIF + minilanguage grammar
  - Output: parsing tree corresponding to the program
  or a message for errors (error diagnose where it is the case)

## Running
```bash
python SLRParser.py "string to check"
```
Example:
```bash
python SLRParser.py "id + ( id * id )"
```
```
## Context Free Grammar
Example from the book `Metode de proiectare a Compilatoarelor, Simona Motogna`
![context free grammar](grammar.png)
###Grammar file:
E -> E + T
E -> T
T -> T * F | F
F -> ( E )
F -> id | const
```

## Bibliography
[Metode de Proiectare a Compilatoarelor, Simona Motogna](https://www.scribd.com/document/332697666/Metode-de-Proiectare-a-Compilatoarelor-Simona-Motogna)
