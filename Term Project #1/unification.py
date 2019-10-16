# Author : Syed Sanzam
# Topic : Unification of Predicate Logic
# Date: 21.09.19

def create():
	global names
	global totArgs
	global args

	names = []
	totArgs = []
	args = []

	for i in range(2):
		t = str(input('Name: '))
		names.append(t)
		t = int(input('Total Number of Arguments: '))
		totArgs.append(t)

		l = []
		for j in range(totArgs[i]):
			t = str(input("Args: "))
			l.append(t)

		args.append(l)
		print('\n')


def display():
	print("The Expressions are : ")
	for i in range(2):
		print(names[i], end = "")
		print('(', end = "")
		for j in range(totArgs[i]):
			print(args[i][j], end="")
			if(j != totArgs[i] - 1):
				print(',',end = "")
		print(')',end = "")
		print('\n')



def isUnifiable():
	sameNames = False
	sameArgs = False

	for i in range(len(names) - 1):
		if(names[i] == names [i + 1]):
			sameNames = True
			break

	for i in range(len(totArgs) - 1):
		if(totArgs[i] == totArgs[i+1]):
			sameArgs = True
			break

	if(sameNames and sameArgs):
		return True
	else:
		return False


def unify():
	global mgu # Most General Unifier
	global substitution # Set of substitution
	global equalityStatements # Set of Equality Statements

	equalityStatements = []
	substitution = []

	for i in range(totArgs[0]):
		l = []
		l.append(args[0][i])
		l.append(args[1][i])
		equalityStatements.append(l)

	loopCount = 0
	while(loopCount <= len(totArgs)):
		#print("While loop e dhukse!")
		l = []
		arg1 = equalityStatements[0][0]
		arg2 = equalityStatements[0][1]
		del equalityStatements[0]

		l.append(arg1) 
		l.append(arg2) 
		
		for i in range(len(equalityStatements)):
			for j in range(len(equalityStatements)):
				if(equalityStatements[i][j] == arg1):
					equalityStatements[i][j] = arg2

		for i in range(len(substitution)):
			for j in range(len(substitution)):
				if(substitution[i][j] == arg1):
					substitution[i][j] = arg2

		substitution.append(l)
		loopCount = loopCount + 1


def printResult():
	file = open("database.txt","a") #To Store the result of the Unification
	print("Most General Unifier (MGU) is : ", end = " ")
	print('[', end = "")
	file.write("[")
	for i in range(len(substitution)):
		print(substitution[i][0] + "/" + substitution[i][1], end = "")
		file.write(substitution[i][0])
		file.write("/")
		file.write(substitution[i][1])
		if(i != len(substitution) - 1):
			print(',',end = " ")
			file.write(",")
	print(']', end = "")
	file.write("]")
	file.write("\n")
	print('\n')




def evaluate():
	if(isUnifiable()):
		unify()
		printResult()
	else:
		print("The Expressions are not Unifiable")



#Main
create()   # Takes input and creates the expressions
display()  # Displays the input expressions
evaluate() # Evaluates and prints the result 

