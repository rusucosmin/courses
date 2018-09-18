member([H | _], H).
member([H | T], E) :-
    H =\= E,
    member(T, E).

append([], E, [E]).
append([H | T], E, X) :-
    append(T, E, Y),
    X = [H | Y].

uniq([], X, X).

uniq([H | T], X, Y) :-
    member(X, H),
    uniq(T, X, Y).

uniq([H | T], X, Y) :-
    not(member(X, H)),
    append(X, H, Z),
    uniq(T, Z, Y).

unique(X, Y) :-
    uniq(X, [], Y).

doIt(H, X, Y, A, B, X1, Y1, A1, B1) :-
    H mod 2 =:= 0,
    X = [H | X1],
    Y = Y1,
    A is A1 + 1,
    B is B1.

doIt(H, X, Y, A, B, X1, Y1, A1, B1) :-
    H mod 2 =:= 1,
    X = X1,
    Y = [H | Y1],
    A is A1,
    B is B1 + 1.

appendList([], X, X).
appendList([H | T], X, Y) :-
    appendList(T, X, Y1),
    Y = [H | Y1].

oddeven([], [], [], 0, 0).
oddeven([H | T], X, Y, A, B) :-
    oddeven(T, X1, Y1, A1, B1),
    doIt(H, X, Y, A, B, X1, Y1, A1, B1).

oddeven(X, Y, A, B) :-
    oddeven(X, ODD, EVEN, A, B),
    appendList(ODD, EVEN, Y).
