myTuple1 = [('Parent','Shahjahan','Arnob'),
		('Parent','Shahjahan','Anik'),
		('Parent','Shahjahan','Adit'),
		('Parent','Shahjahan','Anna'),
		('Parent','Shahjahan','Ashim'),
		('Parent','Ashim','Manha')]


myTuple2 = [('Male','Shahjahan'),
		('Male','Anik'),
		('Male','Arnob'),
		('Male','Adit'),
		('Female','Anna'),
		('Male','Ashim'),
		('Female','Manha')]


totalTuple = len(myTuple1)

def findGender(X):
	tupleLen = len(myTuple2)
	for i in range(tupleLen):
		if(myTuple2[i][1] == X):
			return myTuple2[i][0]

def findBrother(X):
	i = 0
	found = 0

	while(i < totalTuple):
		if(myTuple1[i][0] == 'Parent') & (myTuple1[i][2] == X):
			par = myTuple1[i][1]
			for j in range(totalTuple):
				if(myTuple1[j][0] == 'Parent') & (myTuple1[j][1] == par):
					if(myTuple1[j][2] != X) & (findGender(myTuple1[j][2]) == 'Male'):
						bros = myTuple1[j][2]
						print(bros, end = ' ')
		i = i + 1


def findSister(X):
	i = 0;
	while(i < totalTuple):
		if(myTuple1[i][0] == 'Parent') & (myTuple1[i][2] == X):
			par = myTuple1[i][1]
			for j in range(totalTuple):
				if(myTuple1[j][0] == 'Parent') & (myTuple1[j][1] == par):
					if(myTuple1[j][2] != X) & (findGender(myTuple1[j][2]) == 'Female'):
						sis = myTuple1[j][2]
						print(sis, end = ' ')
		i = i + 1

def findUncle(X):
	i = 0
	while(i  < totalTuple):
		if(myTuple1[i][0] == 'Parent') & (myTuple1[i][2] == X):
			par = myTuple1[i][1]
			findBrother(par)
		i = i + 1

def findAunt(X):
	i = 0
	while(i  < totalTuple):
		if(myTuple1[i][0] == 'Parent') & (myTuple1[i][2] == X):
			par = myTuple1[i][1]
			findSister(par)
		i = i + 1


