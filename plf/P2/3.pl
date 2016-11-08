%merge two lists

removeDup([], []).
removeDup([X], [X]).
removeDup([H | T], X) :-
    removeDup(T, [H1 | Tr]),
    H1 =\= H,
    X = [H, H1 | Tr].

removeDup([H | T], X) :-
    removeDup(T, [H1 | Tr]),
    H1 =:= H,
    X = [H1 | Tr].

append([], E, [E]).
append([H | T], H, [H | T]) :-
    !.
append([H | T], E, [E, H | T]) :-
    !.

merge([], [], []).
merge([], X, Xr) :-
    removeDup(X, Xr).

merge(X, [], Xr) :-
    removeDup(X, Xr).

merge([H1 | T1], [H2 | T2], X) :-
    H2 >= H1,
    merge(T1, [H2 | T2], Tr),
    append(Tr, H1, X).

merge([H1 | T1], [H2 | T2], X) :-
    H1 > H2,
    merge([H1 | T1], T2, Tr),
    append(Tr, H2, X).

merge_hetero([], []).
merge_hetero([H | T], Tr) :-
    number(H),
    merge_hetero(T, Tr).

merge_hetero([H | T], X) :-
    is_list(H),
    merge_hetero(T, Y),
    merge(H, Y, X).
