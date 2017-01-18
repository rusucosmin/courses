insert(E, X, [E | X]).
insert(E, [H | T], [H | Tr]) :-
    insert(E, T, Tr).

perm([], []).
perm([H | T], X) :-
    perm(T, Y),
    insert(H, Y, X).

mabs(X1, X2, X) :-
    X1 >= X2,
    !,
    X is X1 - X2.

mabs(X1, X2, X) :-
    X is X2 - X1.

check([_]).
check([H1, H2 | T]) :-
    mabs(H1, H2, Diff),
    Diff =< 3,
    check([H2 | T]).

solveone(X, Y) :-
    perm(X, Y),
    check(Y).

solve(X, Y) :-
    findall(R, solveone(X, R), Y).


