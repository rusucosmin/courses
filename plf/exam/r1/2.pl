even([]) :- !.
even([_ | T]) :-
    odd(T).

odd([_]) :- !.
odd([_ | T]) :-
    even(T).

addIfOk(H, X, X) :-
    even(H),
    !.
addIfOk(H, X, [H | X]).

mremove([], []).

mremove([H | T], [H | Tr]) :-
    number(H),
    mremove(T, Tr).

mremove([H | T], X) :-
    is_list(H),
    mremove(T, Y),
    addIfOk(H, Y, X).

