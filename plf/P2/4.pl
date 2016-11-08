append([], E, [E]).
append([H | T], E, [H | Tr]) :-
    append(T, E, Tr).

rev([], []).
rev([H | T], X) :-
    rev(T, Y),
    append(Y, H, X).

doSum([], X, 0, X).
doSum([], X, T, [T | X]).

doSum(X, [], 0, X).
doSum(X, [], T, [T | X]).

doSum([H1 | T1], [H2 | T2], T, [SUM | Tr]) :-
    SUM is (H1 + H2 + T) mod 10,
    Tnxt is (H1 + H2 + T) div 10,
    doSum(T1, T2, Tnxt, Tr).

sum(X, Y, Z) :-
    rev(X, X1),
    rev(Y, Y1),
    doSum(X1, Y1, 0, Z1),
    rev(Z1, Z).
