%beautiful <3

discontiguous(odd/1).
discontiguous(even/1).


even([]).

even([_ | T]) :-
    odd(T).
odd([_ | T]) :-
    even(T).

mini(A, B, X) :-
    A >= B,
    X = B.

mini(A, B, X) :-
    B > A,
    X = A.

min([H], H).
min([H | T], X) :-
    min(T, X1),
    mini(H, X1, X).

removeFirst([], _, []).
removeFirst([H | T], H, T) :- !.
removeFirst([H | T], X, [H | Tr]) :-
    removeFirst(T, X, Tr),
    !.

solve(X, Y) :-
    min(X, MIN),
    removeFirst(X, MIN, Y).


