substitute([], _, _, []).

substitute([H | T], H, E2, [E2 | Tr]) :-
    substitute(T, H, E2, Tr).

substitute([H | T], E1, E2, [H | Tr]) :-
    H =\= E1,
    substitute(T, E1, E2, Tr).


aux_sublist([], _, _, _, []).

aux_sublist([_ | T], Ind, M, N, X) :-
    M > Ind,
    NxtInd is Ind + 1,
    aux_sublist(T, NxtInd, M, N, X).

aux_sublist([H | T], Ind, M, N, [H | Tr]) :-
    Ind >= M,
    N >= Ind,
    NxtInd is Ind + 1,
    aux_sublist(T, NxtInd, M, N, Tr).

aux_sublist([_ | _], Ind, _, N, []) :-
    N < Ind.

sublist(X, M, N, Y) :-
    aux_sublist(X, 1, M, N, Y).
