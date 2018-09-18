insert([], E, [E]).
insert([H | T], E, [E, H | T]).
insert([H | T], E, [H | Tr]) :-
    insert(T, E, Tr).


perm([], []).
perm([H | T], Y) :-
    perm(T, X),
    insert(X, H, Y).

comb(0, _, []) :- !.

comb(N, [H | T], [H | Tr]) :-
    N1 is N - 1,
    comb(N1, T, Tr).

comb(N, [_ | T], X) :-
    comb(N, T, X).

check([], S, S).
check([H | T], ACT, S) :-
    ACT1 is ACT + H,
    check(T, ACT1, S).

solveone(K, X, Y, S) :-
    comb(K, X, Z),
    perm(Z, Y),
    check(Y, 0, S).

solve(L, K, S, X) :-
    findall(Y, solveone(K, L, Y, S), X).



