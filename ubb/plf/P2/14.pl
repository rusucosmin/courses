% Author: Cosmin Rusu
% GitHub: github.com/rusucosmin

% Solution for problem 14:
% a. Define a predicate to determine the longest
% sequences of consecutive even numbers (if exist
% more maximal sequences one of them).
% b. For a heterogeneous list, formed from integer
% numbers and list of numbers, define a predicate
% to replace every sublist with the longest sequences 
% of even numbers from that sublist.
% Eg.: [1, [2, 1, 4, 6, 7], 5, [1, 2, 3, 4], 2, [1, 4, 6, 8, 3], 2, [1, 5], 3] => [1, [4, 6], 5, [2], 2, [4, 6, 8], 2, [], 3]

%
%   len(L: list, X: number)
%   flow: (i, o)
%
% computes the length of
% the list, and stores it
% in X.

len([], 0).

len([_ | T], X) :-
    len(T, X1),
    X is X1 + 1.

%
%   getLargest(L1: List, L2: List, L: List)
%   flow: (i, i, o)
%
% stores in L the longest list between
% L1 and L2.

getLargest(X, Y, Z) :-
    len(X, Lx),
    len(Y, Ly),
    Lx > Ly,
    Z = X.

getLargest(X, Y, Z) :-
    len(X, Lx),
    len(Y, Ly),
    Ly >= Lx,
    Z = Y.

%
%   appendIfOk(L: List, E: number, X: List)
%   flow: (i, i, o)
%
% if the element E plus 2 equals the Head of L,
% adds E to the Head of the List and stores the
% result in X
% else, X becomse []

appendIfOk([], H, [H]).

appendIfOk([H | T], E, X) :-
    Next is E + 2,
    H =:= Next,
    X = [E, H | T].

appendIfOk([H | _], E, X) :-
    Next is E + 2,
    H =\= Next,
    X = [].

%   maxi(L: List, X: List, Y: List)
%   flow(i, o, o).
%
% Method to compute the largest suqsequence
% of continous elements in L, and stores it
% in Y.
% In order to do that, it keeps an invariant
% X, which is defined as follows:
%   the longest subsequence satisfying the
%   statement conditions, and begins at the
%   beggining of the list
% So, basically, Y is gonna be the longest
% such X for each suffix of the lisst L.
%

maxi([], [], []).

maxi([H | T], X, Y) :-
    Aux is H mod 2,
    Aux =\= 0,
    maxi(T, _, Y1),
    X = [],
    getLargest(X, Y1, Y).

maxi([H | T], X, Y) :-
    Aux is H mod 2,
    Aux =:= 0,
    maxi(T, X1, Y1),
    appendIfOk(X1, H, X),
    getLargest(X, Y1, Y).

%
% Auxiliary function because we do not actually need
% the X variable from maxi
%
solve(X, Y) :-
    maxi(X, _, Y).

%
% Predicate for nested lists
%
fmm([], []).

fmm([H | T], X) :-
    number(H),
    fmm(T, Tr),
    X = [H | Tr].

fmm([H | T], X) :-
    is_list(H),
    fmm(T, Tr),
    solve(H, Hr),
    X = [Hr | Tr].
