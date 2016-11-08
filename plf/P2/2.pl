%sort list
insert([], [E], E).

insert([H | T], [H | Tr], E) :-
    H < E,
    insert(T, Tr, E).

insert([H | T], [E, H | T], E) :-
    H >= E.

sort_list([], []).
sort_list([H | T], X) :-
    sort_list(T, X1),
    insert(X1, X, H).

sort_nested_list([], []).
sort_nested_list([H | T], [H | Tr]) :-
    number(H),
    sort_nested_list(T, Tr).
sort_nested_list([H | T], [Hr | Tr]) :-
    is_list(H),
    sort_list(H, Hr),
    sort_nested_list(T, Tr).

