import random

def semesterFinal(name): #takes the name of a student as a parameter
	myList = []
	myList = studentInfo.get(name)
	dept = myList[0]
	cgpa = float(myList[1])
	coeff1 =  random.choice((-1, 1))
	coeff2 = random.uniform(0, 1)
	cgpa = cgpa + (coeff1 * coeff2) #randomly changes the cgpa of a student
	cgpa = round(cgpa,2)
	cgpaStr = str(cgpa)
	studentInfo[name] = (dept,cgpa)


#Main

studentInfo = {}
names = []

file = open("input.txt","r")

for line in file:
	(key,val1,val2) = line.split()
	names.append(key)
	studentInfo[key] = (val1,val2)


print(studentInfo)
semesterFinal("Arnob")
print("After Modification : ")
print(studentInfo)
file.close()


file = open("output.txt","w")

for key in studentInfo: 
    myList2 = []
    myList2 = studentInfo.get(key)
    file.write(key)
    file.write(" ")
    file.write(myList2[0])
    file.write(" ")
    file.write(str(myList2[1]))
    file.write("\n")


file.close()
