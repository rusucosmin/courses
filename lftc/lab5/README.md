# SLR Parser

## Usage:
+ Store grammar in a file called `grammar` (all rule must be in format `X->a`, ie LHS and RHS
seperated by -> and no | operator, use only single alphabet for each terminal and non-terminal
eg: i for id)
+ Run `python slr_short.py`
+ Enter grammar file name
+ All GOTO and REDUCTION table is generated
+ Enter string to check
+ Parse table with result is shown

## Context Free Grammar
![context free grammar](grammar.png)

## Bibliography
[Metode de Proiectare a Compilatoarelor, Simona Motogna](https://www.scribd.com/document/332697666/Metode-de-Proiectare-a-Compilatoarelor-Simona-Motogna)

```
S->2afeA    #commands
B->2        #type
B->3        #type
B->4        #type
A->bCc      #compound_stmt
C->CD       #stmt_list
D->Ed       #stmt
D->Fd
D->Gd
D->Hd
D->I
D->J
E->B0       #decl
F->0rM      #assign
L->g        #op
L->h
L->i
L->j
L->k
M->0        #expr
M->1
M->ML0
M->ML1
M->eMf
G->sM       #return
H->N        #iostmt
H->O
N->50       #cin
O->60       #cout
O->61
I->9fPeA    #loop
P->MQM      #condition
Q->l        #rel operator
Q->m
Q->n
Q->o
Q->p
Q->q
J->7fPeA      #if
J->7fPeA8A    #else
```
