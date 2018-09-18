append([], X, X).
append([H | T], X, [H | Tr]) :-
    append(T, X, Tr).


subs([], _, _, []).

subs([H | T], H, X, Y) :-
    subs(T, H, X, Y1),
    append(X, Y1, Y).

subs([H | T], E, X, [H | Y1]) :-
    E =\= H,
    subs(T, E, X, Y1).

removeN([], _, _, []).

removeN([_ | T], N, N, Tr) :-
    NxtInd is N + 1,
    removeN(T, NxtInd, N, Tr).

removeN([H | T], Ind, N, [H | Tr]) :-
    Ind =\= N,
    NxtInd is Ind + 1,
    removeN(T, NxtInd, N, Tr).

remove(X, N, Y) :-
    removeN(X, 1, N, Y).
