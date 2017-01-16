%predicatul initiala
f([], -1).
f([H | T], S) :-
    f(T, S1),
    S1 > 0,
    !,
    S is S1 + H.

f([_ | T], S) :-
    f(T, S1),
    S is S1.

doIt(H, S1, S) :-
    S1 > 0,
    !,
    S is S1 + H.

doIt(H, S1, S) :-
    S is S1.

g([], -1).
g([H | T], S) :-
    g(T, S1),
    doIt(H, S1, S).
