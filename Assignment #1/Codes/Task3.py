tupleList1 = [('Parent','Shahjahan','Arnob'),
		('Parent','Shahjahan','Anik'),
		('Parent','Shahjahan','Arnob'),
		('Parent','Shahjahan','Anna'),
		('Parent','Shahjahan','Ashim'),
		('Parent','Ashim','Manha')]

X = str(input("Grandchild: "))

print("Grandparent : ", end = ' ')
i = 0;
tupLen = len(tupleList1)
while(i < tupLen):
	if(tupleList1[i][0] == 'Parent')&(tupleList1[i][2] == X):
		par = tupleList1[i][1]
		for j in range(tupLen):
			if(tupleList1[j][0] == 'Parent') & (tupleList1[j][2] == par):
				grandpar = tupleList1[j][1]
				print(grandpar, end = ' ')
	i = i + 1;



