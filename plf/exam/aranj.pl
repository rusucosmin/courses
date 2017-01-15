check([], X, X).
check([H | T], X, Y) :-
    X1 is X * H,
    check(T, X1, Y).

arr(K, X, R) :-
    comb(K, X, R1),
    perm(R1, R).

comb(0, _, []).
comb(K, [H | T], [H | Tr]) :-
    K > 0,
    K1 is K - 1,
    comb(K1, T, Tr).

comb(K, [_ | T], Y) :-
    K > 0,
    comb(K, T, Y).

insert([], E, [E]).
insert([H | T], E, [E, H | T]).
insert([H | T], E, [H | Tr]) :-
    insert(T, E, Tr).

perm([], []).
perm([H | T], X) :-
    perm(T, X1),
    insert(X1, H, X).

onesol(K, X, P, Y) :-
    arr(K, X, Y),
    check(Y, 1, P).

solve(K, X, P, Y) :-
    findall(R, onesol(K, X, P, R), Y).
