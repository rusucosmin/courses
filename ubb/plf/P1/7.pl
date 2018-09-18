%   7.
%   a. Write a predicate to compute the intersection of two sets.
% b. Write a predicate to create a list (m, ..., n) of all integer numbers from the interval [m, n].


member([X | _], X).
member([_ | T], X) :-
    member(T, X).

inter([], _, []).

inter([H | T], L2, X) :-
    member(L2, H),
    inter(T, L2, Tr),
    X = [H | Tr].

inter([H | T], L2, X) :-
    not(member(L2, H)),
    inter(T, L2, X).


%b

genList(M, N, []) :-
    M > N.

genList(M, N, X) :-
    NEWM is M + 1,
    N >= M,
    genList(NEWM, N, Y),
    X = [M | Y].
