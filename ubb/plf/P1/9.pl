insert(X, E, 0, [E | X]) :- !.
insert([], _, _, []).

insert([H | T], E, POS, [H |  X]) :-
    POS1 is POS - 1,
    insert(T, E, POS1, X).

gcd(A, 0, A).
gcd(A, B, X) :-
    not(B =:= 0),
    NXT is A mod B,
    gcd(B, NXT, X).

gcdList([E], E).
gcdList([H | T], X) :-
    gcdList(T, X1),
    gcd(H, X1, X).
