remove([], _, []).
remove(X, 0, X).

remove([H | T], K, Tr) :-
    K > 0,
    Mod is H mod 2,
    Mod > 0,
    K1 is K - 1,
    remove(T, K1, Tr).

remove([H | T], K, [H | Tr]) :-
    K > 0,
    Mod is H mod 2,
    Mod == 0,
    remove(T, K, Tr).

