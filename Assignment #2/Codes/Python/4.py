# Well this doesn't work for every scenario, needs to be fixed.

graph = [('i','a',35),
		('i','b',45),
		('a','c',22),
		('a','d',32),
		('b','d',28),
		('b','e',36),
		('b','f',27),
		('c','d',31),
		('c','g',47),
		('d','g',30),
		('e','g',26),
		]

totalTuple = len(graph)

def isNeighbor(n1,n2):
	i = 0
	value = -1
	while(i < totalTuple):
		if(graph[i][0] == n1):
			for j in range(totalTuple):
				if(graph[j][0] == n1 and graph[j][1] == n2):
					value = graph[j][2]
		i = i + 1

	return value


def findCommonNode(n1,n2):
	commonNode = []
	for i in range(totalTuple):
		if(graph[i][0] == n1):
			temp = graph[i][1]
			for j in range(totalTuple):
				if(graph[j][0] == temp and graph[j][1] == n2):
					commonNode.append(temp)
	return commonNode


def pathLength(n1,n2):
	if(isNeighbor(n1,n2) != -1):
		return isNeighbor(n1,n2)
	else: 
		myList = findCommonNode(n1,n2)
		m = myList[0] 
		return isNeighbor(n1,m) + isNeighbor(m,n2)


#Main 
t = int(input('How many times?'))
for i in range(t):
	print('iteration: ', i+1)
	n1 = str(input('Source Node : '))
	n2 = str(input('Destination Node : '))
	print('Pathlength : ',pathLength(n1,n2))
	print('\n')
