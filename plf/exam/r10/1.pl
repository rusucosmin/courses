member(X, [X | _]) :- !.
member(X, [_ | Tr]) :-
    member(X, Tr).

toSet([], []).
toSet([H | T], Tr) :-
    toSet(T, Tr),
    member(H, Tr).

toSet([H | T], [H | Tr]) :-
    toSet(T, Tr),
    not(member(H, Tr)).

toSetCol([], X, X).
toSetCol([H | T], Y, X) :-
    member(H, Y),
    toSetCol(T, Y, X).

toSetCol([H | T], Y, X) :-
    not(member(H, Y)),
    toSetCol(T, [H | Y], X).

toSetSmen(X, Y) :-
    toSetCol(X, [], Y).
