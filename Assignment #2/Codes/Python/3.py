def findSum(N,firstElement,interval):
	if(N == 0):
		return 0
	if(N == 1):
		return firstElement
	else:
		return findSum(N-1,interval,firstElement) + firstElement + (N-1) * interval

#Main

t = int(input('How many times?'))
for i in range(t):
	print('Iteration: ', i+1)
	n = int(input('N : '))
	f = int(input('First Element : '))
	i = int(input('Interval : '))
	print('Sum is : ', findSum(n,f,i))
	print('\n')

