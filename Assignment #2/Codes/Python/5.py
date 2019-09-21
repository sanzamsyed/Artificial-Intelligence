def findManhattanDistance():
	goalState=[(1,1,1), (2,1,2), (3,1,3), (4,2,3), (5,3,3), (6,3,2), (7,3,1), (8,2,1)]
	gblnk = (2,2)
	currentState=[(1,1,2), (2,1,3), (3,2,1), (4,2,3), (5,3,3), (6,2,2), (7,3,2), (8,1,1)]
	blnk = (3,1)
	totalTuple = len(goalState)
	totalDistance = 0
	i = 0
	while(i < totalTuple):
		temp = currentState[i][0] 
		for j in range(totalTuple):
			if(goalState[j][0] == temp):
				totalDistance = totalDistance + abs(currentState[j][1] - goalState[j][1]) + abs(currentState[j][2] - goalState[j][2]) # abs(x1-x2) + abs(y1-y2)
		i = i+1
	return totalDistance

#Main
print('Tota distance :', findManhattanDistance())
print('\n')

