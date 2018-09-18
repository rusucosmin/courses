candidate([H | _], H).
candidate([_ | T], X) :-
    candidate(T, X).
