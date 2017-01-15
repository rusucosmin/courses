gen(N, Pos, []) :-
    Pos is N * 2,
    !.

gen(N, Pos, [Pos | Tr]) :-
    Pos1 is Pos + 1,
    gen(N, Pos1, Tr).

insert(X, E, [E | X]).
insert([H | T], E, [H | X]) :-
    insert(T, E, X).

perm([], []).
perm([H | T], X) :-
    perm(T, Y),
    insert(Y, H, X).

mabs(X, X1, X2) :-
    X1 >= X2,
    !,
    X is X1 - X2.

mabs(X, X1, X2) :-
    X is X2 - X1.

check([_]).
check([H1, H2 | T]) :-
    mabs(Diff, H1, H2),
    2 >= Diff,
    check([H2 | T]).

solveone(X, Y) :-
    perm(X, Y),
    check(Y).

main(N, X) :-
    gen(N, N, L),
    findall(R, solveone(L, R), X).
