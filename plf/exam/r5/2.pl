prim(N, N) :-
    N >= 2,
    !.

prim(N, D) :-
    N >= 2,
    Mod is N mod D,
    Mod > 0,
    D1 is D + 1,
    prim(N, D1).

remove(X, 0, X) :- !.
remove([], _, []) :- !.

remove([H | T], N, Tr) :-
    prim(H, 2),
    !,
    N1 is N - 1,
    remove(T, N1, Tr).

remove([H | T], N, [H | Tr]) :-
    remove(T, N, Tr).
