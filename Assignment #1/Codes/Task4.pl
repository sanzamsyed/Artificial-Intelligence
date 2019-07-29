parent('Shahjahan','Arnob').
parent('Shahjahan','Adit').
parent('Shahjahan','Anik').
parent('Shahjahan','Anna').
parent('Shahjahan','Amit').
parent('Shahjahan','Ashim').
parent('Ashim','Manha').


male('Arnob').
male('Anik').
male('Adit').
male('Ashim').
male('Amit').

female('Anna').

brother(X,Y):-
	parent(Z,X),
	parent(Z,Y),
	male(X),
	not(X = Y).


sister(X,Y):-
	parent(Z,X),
	parent(Z,Y),
	female(X),
	not(X = Y).

uncle(X,Y):-
	brother(X,Z),
	parent(Z,Y).

aunt(X,Y):-
	sister(X,Z),
	parent(Z,Y).


