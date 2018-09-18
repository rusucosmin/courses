member(H, [H | _]).
member(E, [_ | T]) :-
    member(E, T).

addIfOkay(H, Tr, X) :-
    member(H, Tr),
    X = Tr.

addIfOkay(H, Tr, X) :-
    not(member(H, Tr)),
    X = [H | Tr].

toset([], []).
toset([H | T], X) :-
    toset(T, Tr),
    addIfOkay(H, Tr, X).

toset([], X, X).
toset([H | T], Y, X) :-
    not(member(H, Y)),
    toset(T, [H | Y], X).

toset([H | T], Y, X) :-
    member(H, Y),
    toset(T, Y, X).
