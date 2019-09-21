sum(1,FirstElement,_,FirstElement):- !.
sum(N,FirstElement,Interval,Result):-
	N1 is N-1,
	sum(N1,FirstElement,Interval,TemporaryResult),
	Result is TemporaryResult + FirstElement + (N - 1) * Interval.