sum(0, 0) :- !.

sum(N, S) :-
    N1 is N - 1,
    sum(N1, S1),
    S is S1 + N * 3.

sumsmen(0, X, X) :- !.
sumsmen(N, S, X) :-
    N1 is N - 1,
    S1 is S + N * 3,
    sumsmen(N1, S1, X).


