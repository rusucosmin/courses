subset([], []).
subset([_ | T], Tr) :-
    subset(T, Tr).
subset([H | T], [H | Tr]) :-
    subset(T, Tr).


