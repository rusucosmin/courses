remove([H | T], H, T).

remove([H | T], E, [H | Tr]) :-
    remove(T, E, Tr).


perm(0, []).

perm(N, X) :-
    N > 0,
    N1 is N - 1,
    perm(N1, Y),
    remove(X, N, Y).

getPerm(N, X) :-
    findall(Y, perm(N, Y), X),
    write(X).
