append([], X, X).
append([H | T], X, Y) :-
    append(T, X, Y1),
    Y = [H | Y1].

subs([], _, _, []).
subs([E | T], E, X, Y) :-
    subs(T, E, X, Y1),
    append(X, Y1, Y).

subs([H | T], E, X, [H | Tr]) :-
    H =\= E,
    subs(T, E, X, Tr).

replace([], _, []).

replace([H | T], X, [H | Tr]) :-
    number(H),
    replace(T, X, Tr).

replace([[Hi | Ti] | T], X, Y) :-
    is_list([Hi | Ti]),
    replace(T, X, Y1),
    subs([Hi | Ti], Hi, X, Z),
    Y = [Z | Y1].

