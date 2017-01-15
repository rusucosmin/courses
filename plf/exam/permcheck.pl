insert([], E, [E]).
insert([H | T], E, [E, H | T]).
insert([H | T], E, [H | Tr]) :-
    insert(T, E, Tr).

perm([], []).
perm([H | T], X) :-
    perm(T, Y),
    insert(Y, H, X).

generate(N, Pos, []) :-
    Pos is 2 * N,
    !.

generate(N, Pos, [Pos | Tr]) :-
    Pos1 is Pos + 1,
    generate(N, Pos1, Tr).

mabs(X1, X2, Y) :-
    X1 >= X2,
    Y is X1 - X2,
    !.

mabs(X1, X2, Y) :-
    Y is X1 - X2.

check([]).
check([_]).
check([H1, H2 | T]) :-
    mabs(H1, H2, Diff),
    2 >= Diff,
    check([H2 | T]).

solve(N, Y) :-
    generate(N, N, X),
    perm(X, Y),
    check(Y).

