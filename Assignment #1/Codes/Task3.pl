parent('Shahjahan','Arnob').
parent('Shahjahan','Adit').
parent('Shahjahan','Anik').
parent('Shahjahan','Anna').
parent('Shahjahan','Amit').
parent('Shahjahan','Ashim').
parent('Ashim','Manha').



grandchild(X,Z):-
	parent(Z,Y),
	parent(Y,X).


findGp:-
	write('Grandkid: '),
	read(X),
	write('Grandparent: '),
	grandchild(X,Gp),
	write(Gp),
	tab(5),
	fail.