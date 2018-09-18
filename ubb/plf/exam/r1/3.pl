subs([], [], 0).

subs([_ | T], Tr, S) :-
    subs(T, Tr, S).

subs([H | T], [H | Tr], S) :-
    S1 is S - H,
    subs(T, Tr, S1).

solve(X, S, Y) :-
    findall(R, subs(X, R, S), Y).
