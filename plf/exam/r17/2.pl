max(X1, X2, X1) :-
    X1 > X2,
    !.

max(X1, X2, X2).

maxlist([X], X) :- !.
maxlist([H | T], X) :-
    number(H),
    !,
    maxlist(T, X1),
    max(X1, H, X).

erase([], _, []).
erase([H | T], H, Tr) :-
    !,
    erase(T, H, Tr).

erase([H | T], X, [H | Tr]) :-
    erase(T, X, Tr).

remove([], []).
remove([H | T], [H | Tr]) :-
    number(H),
    !,
    remove(T, Tr).

remove([H | T], [H1 | Tr]) :-
    maxlist(H, MAXH),
    erase(H, MAXH, H1),
    remove(T, Tr).




