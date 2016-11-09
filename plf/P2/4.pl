append([], E, [E]).
append([H | T], E, [H | Tr]) :-
    append(T, E, Tr).

rev([], []).
rev([H | T], X) :-
    rev(T, Y),
    append(Y, H, X).

doSum([], [], 0, []) :- !.
doSum([], [], T, [T]) :- !.
doSum([], X, 0, X) :- !.
doSum(X, [], 0, X) :- !.

doSum([], [H | T], Tra, [Hr | Tr]) :-
    Hr is (H + Tra) mod 10,
    NewTr is (H + Tra) div 10,
    doSum([], T, NewTr, Tr).

doSum(X, [], Tra, Y) :-
    doSum([], X, Tra, Y).

doSum([H1 | T1], [H2 | T2], T, [SUM | Tr]) :-
    SUM is (H1 + H2 + T) mod 10,
    Tnxt is (H1 + H2 + T) div 10,
    doSum(T1, T2, Tnxt, Tr).

sum(X, Y, Z) :-
    rev(X, X1),
    rev(Y, Y1),
    doSum(X1, Y1, 0, Z1),
    rev(Z1, Z).

sum_hetero([], []).
sum_hetero([H | T], X) :-
    number(H),
    sum_hetero(T, X).

sum_hetero([H | T], X) :-
    is_list(H),
    sum_hetero(T, X1),
    sum(X1, H, X).
