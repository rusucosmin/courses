append([], X, X).
append([H | T], X, Y) :-
    append(T, X, Y1),
    Y = [H | Y1].

pair_aux(_, [], []).
pair_aux(E, [H | T], X) :-
    pair_aux(E, T, X1),
    X = [[E, H] | X1].

pair([], []).
pair([H | T], X) :-
    pair(T, Y),
    pair_aux(H, T, X1),
    append(X1, Y, X).

member([H | _], H).

member([_ | T], E) :-
    member(T, E).

pair_smen([H | T], X) :-
    member(T, M),
    X = [H, M].

pair_smen([_ | T], X) :-
    pair_smen(T, X).

getPairs(L, X) :-
    findall(P, pair_smen(L, P), X).
