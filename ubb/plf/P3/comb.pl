comb(0, _, []).

comb(N, [X | T], [X | Tr]) :-
    N > 0,
    N1 is N - 1,
    comb(N1, T, Tr).

comb(N, [_ | T], Tr) :-
    N > 0,
    comb(N, T, Tr).

main(N, X, Y) :-
    findall(AUX, comb(N, X, AUX), Y).
