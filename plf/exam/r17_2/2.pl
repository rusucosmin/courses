toBeDeleted(N) :-
    N > 1,
    N1 is N - 2,
    Mod is N1 mod 4,
    Mod =:= 0.

remove(_, [], []).
remove(P, [_ | T], Tr) :-
    toBeDeleted(P),
    !,
    P1 is P + 1,
    remove(P1, T, Tr).

remove(P, [H | T], [H | Tr]) :-
    P1 is P + 1,
    remove(P1, T, Tr).

solve(X, Y) :-
    remove(1, X, Y).

