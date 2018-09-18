insert(E, X, [E | X]).
insert(E, [H | T], [H | Tr]) :-
    insert(E, T, Tr).

perm([], []).
perm([H | T], X) :-
    perm(T, Y),
    insert(H, Y, X).

comb(0, _, []) :- !.
comb(K, [H | T], [H | Tr]) :-
    K1 is K - 1,
    comb(K1, T, Tr).

comb(K, [_ | T], Tr) :-
    comb(K, T, Tr).

check([], 0).
check([H | T], S) :-
    S1 is S - H,
    check(T, S1).

solveone(X, K, S, Y) :-
    comb(K, X, C),
    perm(C, Y),
    check(Y, S).

solve(X, K, S, Y) :-
    findall(R, solveone(X, K, S, R), Y).

