gen(N, M, []) :-
    M is 2 * N - 1,
    !.

gen(N, M, [M | Tr]) :-
    M1 is M + 1,
    gen(N, M1, Tr).

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

check([]).
check([_]).
check([H1, H2 | T]) :-
    mabs(H1, H2, Diff),
    Diff =< 2,
    check([H2 | T]).

solveone(N, X) :-
    gen(N, N, L),
    perm(L, X),
    check(X).

solve(N, X) :-
    findall(R, solveone(N, R), X).

