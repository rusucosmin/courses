is_pow_2(1) :- !.
is_pow_2(X) :-
    X1 is X / 2,
    floor(X1, Y),
    X1 is Y,
    is_pow_2(X1).

is_pow(K, N) :-
    X is K / N,
    floor(X, Y),
    X is Y,
    is_pow_2(X).

remove_aux([], _, _, []).
remove_aux([_ | T], N, K, Tr) :-
    is_pow(K, N),
    !,
    K1 is K + 1,
    remove_aux(T, N, K1, Tr).

remove_aux([H | T], N, K, [H | Tr]) :-
    K1 is K + 1,
    remove_aux(T, N, K1, Tr).


remove(R, N, X) :-
    remove_aux(R, N, 1, X).
