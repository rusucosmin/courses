member([H | T], H).
member([_ | T], H) :-
    member(T, H).

isset([]).
isset([Ha | Ta]) :-
    not(member(Ta, Ha)),
    isset(Ta).

remove([], E, _, []).
remove(X, E, 0, X).

remove([H | T], H, X, Y) :-
    X1 is X - 1,
    remove(T, H, X1, Y).

remove([H | T], E, X, [H | Tr]) :-
    not(H =:= E),
    remove(T, E, X, Tr).
