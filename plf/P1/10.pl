valley_inc([_]).

valley_inc([H1, H2 | T]) :-
    H1 < H2,
    valley_inc([H2 | T]).

valley_dec([H1, H2 | T]) :-
    H2 < H1,
    valley_dec([H2 | T]).

valley_dec([H1, H2 | T]) :-
    H1 < H2,
    valley_inc([H1, H2 | T]).

valley([H1, H2 | T]) :-
    H2 < H1,
    valley_dec([H1, H2 | T]).

ssum([], 0, _).
ssum([H | T], SUM, SIGN) :-
    SIGN1 is SIGN * (-1),
    ssum(T, SUM1, SIGN1),
    SUM is SUM1 + H * SIGN.


sum(X, S) :-
    ssum(X, S, 1).
