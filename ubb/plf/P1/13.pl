member([H | _], H).

member([H | T], E) :-
    E =\= H,
    member(T, E).

make_set([], []).

make_set([H | T], X) :-
    make_set(T, Y),
    member(Y, H),
    X = Y.

make_set([H | T], X) :-
    make_set(T, Y),
    not(member(Y, H)),
    X = [H | Y].

gcd(A, 0, A) :- !.

gcd(A, B, X) :-
    C is A mod B,
    gcd(B, C, X).

gcdList([E], E).
gcdList([H | T], X) :-
    gcdList(T, Y),
    gcd(H, Y, X).
