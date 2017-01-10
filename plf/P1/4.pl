member([H | _], H).
member([_ | T], H) :-
    member(T, H).

diff([], _, []).

diff([H | T], B, [H | Tr]) :-
    not(member(B, H)),
    diff(T, B, Tr).

diff([H | T], B, Tr) :-
    member(B, H),
    diff(T, B, Tr).

insert1([], []).

insert1([H | T], [H | Tr]) :-
    H mod 2 =\= 0,
    insert1(T, Tr).

insert1([H | T], X) :-
    H mod 2 =:= 0,
    insert1(T, Y),
    X = [H, 1 | Y].
