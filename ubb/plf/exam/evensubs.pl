subset([], []).
subset([H | T], [H | Tr]) :-
    subset(T, Tr).
subset([_ | T], Tr) :-
    subset(T, Tr).

len([], 0).
len([_ | T], N) :-
    len(T, N1),
    N is N1 + 1.

evensub(X, Y) :-
    subset(X, Y),
    len(Y, N),
    AUX is N mod 2,
    AUX is 0.

solve(X, Y) :-
    findall(R, evensub(X, R), Y).
