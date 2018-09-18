pow(_, 0, 1).
pow(X, N, Y) :-
    N > 0,
    N1 is N - 1,
    pow(X, N1, Y1),
    Y is Y1 * X.

