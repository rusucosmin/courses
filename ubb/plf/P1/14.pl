remove([H | T], H, T).

remove([H | T], E, [H | Tr]) :-
    H =\= E,
    remove(T, E, Tr).

eqset([], []).

eqset([H1 | T1], X) :-
    remove(X, H1, Y),
    eqset(T1, Y).

getNth([H | _], 1, H).

getNth([_ | T], N, X) :-
    N > 1,
    N1 is N - 1,
    getNth(T, N1, X).
