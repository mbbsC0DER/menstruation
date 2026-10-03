% ---------- Facts ----------

male(arjun).
male(rohan).
male(vikram).
male(karan).
male(aman).
male(raj).
male(varun).

female(priya).
female(neha).
female(riya).
female(ananya).
female(kavya).
female(meera).
female(diya).

% parent(Parent, Child)
parent(arjun, rohan).
parent(priya, rohan).
parent(arjun, riya).
parent(priya, riya).
parent(rohan, karan).
parent(neha, karan).
parent(rohan, ananya).
parent(neha, ananya).
parent(vikram, kavya).
parent(meera, kavya).
parent(vikram, aman).
parent(meera, aman).
parent(karan, varun).
parent(ananya, diya).

% ---------- Rules ----------

% Father
father(X, Y) :-
    male(X),
    parent(X, Y).

% Mother
mother(X, Y) :-
    female(X),
    parent(X, Y).

% Grandfather
grandfather(X, Y) :-
    male(X),
    parent(X, Z),
    parent(Z, Y).

% Grandmother
grandmother(X, Y) :-
    female(X),
    parent(X, Z),
    parent(Z, Y).

% Brother
brother(X, Y) :-
    male(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Sister
sister(X, Y) :-
    female(X),
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Uncle
uncle(X, Y) :-
    male(X),
    parent(P, Y),
    brother(X, P).

% Aunt
aunt(X, Y) :-
    female(X),
    parent(P, Y),
    sister(X, P).

% Nephew
nephew(X, Y) :-
    male(X),
    (uncle(Y, X) ; aunt(Y, X)).

% Niece
niece(X, Y) :-
    female(X),
    (uncle(Y, X) ; aunt(Y, X)).

% Cousin
cousin(X, Y) :-
    parent(P1, X),
    parent(P2, Y),
    (brother(P1, P2) ; sister(P1, P2)),
    X \= Y.

% Queries from Notes_260912_182345.PDF:
% ?- father(arjun, rohan).
% ?- mother(priya, riya).
% ?- grandfather(arjun, karan).
% ?- grandmother(priya, ananya).
% ?- brother(riya, rohan).
% ?- sister(riya, rohan).
% ?- uncle(vikram, varun).
% ?- aunt(meera, varun).
% ?- cousin(karan, diya).
% The final three queries are false with these facts, unlike the PDF answers.
