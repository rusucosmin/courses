% 1.
% a. Write a predicate to determine the lowest common multiple of a list formed from integer numbers.
% b. Write a predicate to add a value v after 1-st, 2-nd, 4-th, 8-th, … element in a list.
%
% gcd(X: int, Y: int, Z: int)
%   computes the gcd between X and Y and stores it in Z
%   flow model (i, i, o).
%
%

gcd(X, 0, X).

gcd(X, Y, Z) :-
    number(X),
    number(Y),
    Mod is mod(X, Y),
    gcd(Y, Mod, Z).

gcdList([], 0).
gcdList([X], X).

gcdList([H | T], X) :-
    gcdList(T, Y),
    gcd(H, Y, X).

lcmList([], 0).
lcmList([X], X).

lcmList([H | T], X) :-
    lcmList(T, Y),
    gcd(H, Y, Z),
    X is (H * Y) / Z.

isPow(1, X).

isPow(X, Y) :-
    0 is mod(X, Y),
    Z is X / Y,
    isPow(Z, Y).

addPower([], X, Y, [X]) :-
    isPow(Y, 2).

addPower([], X, Y, []) :-
    not(isPow(Y, 2)).

addPower([H | T], X, Y, [H | Tr]) :-
    not(isPow(Y, 2)),
    addPower(T, X, Y + 1, Tr).

addPower([H | T], X, Y, [H, X | Tr]) :-
    isPow(Y, 2),
    addPower(T, X, Y + 1, Tr).
