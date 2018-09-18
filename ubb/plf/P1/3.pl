nocc([], _, 0).

nocc([Y | T], Y, Z) :-
    nocc(T, Y, Z1),
    Z is Z1 + 1.

nocc([_ | T], Y, Z) :-
    nocc(T, Y, Z).

remDup([], _, []).

remDup([H | T], X, Y) :-
    remDup(T, X, Y1),
    nocc(X, H, Cnt),
    (Cnt =:= 1 ->
    Y = [H | Y1];
    Y = Y1).

uniq(X, Y) :-
    remDup(X, X, Y).

max([X], X).

max([H | T], X) :-
    max(T, Y),
    ( H < Y ->
        X = Y;
      X = H).

remove([], [], _).

remove([H | T], Y, H) :-
    remove(T, Y, H).

remove([H | T], Y, X) :-
    remove(T, Z, X),
    Y = [H | Z].


remMax(X, Y) :-
    max(X, Z),
    remove(X, Y, Z).

