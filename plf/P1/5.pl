member([H | _], H).
member([_ | T], E) :-
    member(T, E).

union([], [], []).

union([], A, A).

union([H | T], B, [H | Tr]) :-
    not(member(B, H)),
    union(T, B, Tr).

union([H | T], B, X) :-
    member(B, H),
    union(T, B, X).

append([], X, X).
append([H | T], Y, X) :-
    append(T, Y, X1),
    X = [H | X1].

allPairs(H, [], []).
allPairs(H, [Ha | Ta], X) :-
    H == Ha,
    allPairs(H, Ta, X).

allPairs(H, [Ha | Ta], [[H, Ha] | X]) :-
    not(H == Ha),
    allPairs(H, Ta, X).

prod([], []).

prod([Ha | Ta], X) :-
    prod(Ta, X1),
    allPairs(Ha, Ta, X2),
    append(X2, X1, X).
