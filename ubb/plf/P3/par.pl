par_aux(0, 0, "").

par_aux(N, O, X) :-
    N > 0,
    O >= 0,
    O1 is O + 1,
    N1 is N - 1,
    par_aux(N1, O1, Y),
    string_concat("(", Y, X).
  %  X = ['('| Y].

par_aux(N, O, X) :-
    N > 0,
    O > 0,
    O1 is O - 1,
    N1 is N - 1,
    par_aux(N1, O1, Y),
    string_concat(")", Y, X).
  %  X = [')' | Y].

par(N, X) :-
    findall(P, par_aux(N, 0, P), X).
