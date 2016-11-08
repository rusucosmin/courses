%unique sort list
%insert(X: list, Y: list, E: number)
% (i, o, i)
% inserts the element E in the
% sorted list X while keeping 
% the list sorted

%empty list
insert([], [E], E).
%if E already exists, Y is the same as X
insert([E | X], [E | X], E).

insert([H | T], Y, E) :-
    H < E,
    insert(T, T1, E),
    Y = [H | T1].

insert([H | T], Y, E) :-
    H > E,
    Y = [E, H | T].

sort_unique([], []).
sort_unique([H | T], Y) :-
    sort_unique(T, Y1),
    insert(Y1, Y, H).


sort_nested([], []).
sort_nested([H | T], [H | Tr]) :-
    number(H),
    sort_nested(T, Tr).

sort_nested([H | T], [H1 | Tr]) :-
    is_list(H),
    sort_unique(H, H1),
    sort_nested(T, Tr).
