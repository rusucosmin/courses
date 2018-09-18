subs([], [], 0).
subs([_ | T], Tr, S) :-
    subs(T, Tr, S).

subs([H | T], [H | Tr], S) :-
    News is S - H,
    subs(T, Tr, News).

solve(X, S, Y) :-
    findall(R, subs(X, R, S), Y).


