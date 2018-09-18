insert(E, X, [E | X]).
insert(E, [H | T], [H | Tr]) :-
    insert(E, T, Tr).

perm([], []).
perm([H | T], X) :-
    perm(T, Y),
    insert(H, Y, X).

comb(0, _, []) :- !.
comb(N, [H | T], [H | Tr]) :-
    N1 is N - 1,
    comb(N1, T, Tr).
comb(N, [_ | T], Tr) :-
    comb(N, T, Tr).

check([], 0).
check([H | T], S) :-
    S1 is S - H,
    check(T, S1).


findone(X, K, S, Y) :-
    comb(K, X, R),
    perm(R, Y),
    check(Y, S).

solve(X, K, S, Y) :-
    findall(R, findone(X, K, S, R), Y).
