remove([], X, []).

remove([H | T], X, Tr) :-
    H = X,
    remove(T, X, Tr).

remove([H | T], X, [H | Tr]) :-
    H \= X,
    remove(T, X, Tr).

occ([], X, 0).
occ([H | T], X, Y) :-
    H = X,
    occ(T, X, Z),
    Y is Z + 1.

occ([H | T], X, Y) :-
    H \= X,
    occ(T, X, Y).

numberAtom([], []).

numberAtom([H | T], [[H, X] | Tr]) :-
    occ([H | T], H, X),
    remove([H | T], H, Z),
    numberAtom(Z, Tr).
