f([], 0).
f([H | T], S) :-
    f(T, S1),
    S1 >= 2,
    !,
    S is S1 + H.

f([_ | T], S) :-
    f(T, S1),
    S is S1 + 1.

add(S1, H, S) :-
    S1 >= 2,
    !,
    S is S1 + H.

add(S1, _, S) :-
    S is S1 + 1.

g([], 0).
g([H | T], S) :-
    g(T, S1),
    add(S1, H, S).
