progr([_]).
progr([_ , _]).
progr([H1, H2, H3 | T]) :-
    S is H1 + H3,
    AVG is S / 2,
    H2 =:= AVG,
    progr([H2, H3 | T]).

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

isprogr(Y, X) :-
    perm(Y, X),
    progr(X),
    !.

solveone(X, K, Y) :-
    comb(K, X, C),
%   perm(C, Y),
    isprogr(C, Y).

solve(X, K, Y) :-
    findall(R, solveone(X, K, R), Y).

