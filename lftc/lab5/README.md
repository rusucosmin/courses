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
## Context Free Grammar
Example from the book `Metode de proiectare a Compilatoarelor, Simona Motogna`

### Step 1 Grammar file:
```
E -> E + T
E -> T
T -> T * F | F
F -> ( E )
F -> id | const
```

In order to test this grammar with an input sequence run
`./step1.sh "id * (id + id)"`
### Step 2 Grammar file:
```
E -> int main opar epar COMP_STMT
TYPE -> int | float | char
COMP_STMT -> obrace STMT_LIST ebrace
STMT_LIST -> STMT_LIST STMT | STMT
STMT -> ASSIGN | DECL | RETURN | IOSTMT | LOOP | IF_STMT | semicolon
ASSIGN -> id assign EXPR semicolon
DECL -> TYPE id semicolon
RETURN -> return EXPR semicolon
IOSTMT -> cin id semicolon | cout EXPR semicolon
PASS -> pass semicolon
OP -> plus | minus | mult | div | mod
EXPR -> id | const | EXPR OP const | EXPR OP id | opar EXPR epar
LOOP -> while opar COND epar COMP_STMT
COND -> EXPR RELATION_OP EXPR
RELATION_OP -> eq | noteq | lt| le | gt | ge
IF_STMT -> if opar COND epar COMP_STMT else COMP_STMT
```

In order to test this grammar with an input sequence run
`./step2.sh main.cpp`

## Bibliography
[Metode de Proiectare a Compilatoarelor, Simona Motogna](https://www.scribd.com/document/332697666/Metode-de-Proiectare-a-Compilatoarelor-Simona-Motogna)
