insert(E, X, [E | X]).              %add on the head
insert(E, [H | T], [H | Tr]) :-     %add after the head
    insert(E, T, Tr).

perm([], []) :- !.
perm([H | T], X) :-
    perm(T, Y),
    insert(H, Y, X).

comb(0, _, []).
comb(K, [H | T], [H | Tr]) :-
    K > 0,
    K1 is K - 1,
    comb(K1, T, Tr).
comb(K, [_ | T], Tr) :-
    K > 0,
    comb(K, T, Tr).

aranj(K, X, Y) :-
    comb(K, X, C),
    perm(C, Y).

check([], 0).
check([H | Tr], S) :-
    S1 is S - H,
    check(Tr, S1).

solveone(X, K, S, Y) :-
    aranj(K, X, Y),
    check(Y, S).

solve(X, K, S, Y) :-
    findall(R, solveone(X, K, S, R), Y).




