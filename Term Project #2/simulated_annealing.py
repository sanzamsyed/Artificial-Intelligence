#Barely Works

import sys
count = 1  
initState = [2,3,4,5,6,5,7,8]  
  
def generateSuccessor():  
    global initState  
    initState = [2,3,4,5,6,5,7,8]  
    state = initState  
    length = len(initState)  
    successorVal = 1  
  
    for i in range(length):  
        indexVal = initState[i]  
        for j in range(length):  
            if(successorVal != indexVal):  
                state[i] = successorVal  
                #print(state)  
                findNAP(state)  
            successorVal = successorVal + 1  
  
        print('\n')  
        #initState = [2,3,4,5,6,5,7,8] 
        state = initState   
        successorVal = 1  
  
def findNAP(state):  
    #Init Variables  
    row = 8  
    col = 8  
    length = len(state)  
    matrix = [[0 for i in range(col+1)]for j in range(row+1)]  
    sameRow = 0  
    n = 0  
    global count  
    global initState  
      
    #Init matrix with 0-Based Index  
    for i in range(length):  
        matrix[i][state[i] - 1] = 1  
  
    #Calculate Attacking Pair of Queens  
    for i in range(row):  
        for j in range(col):  
            if(matrix[i][j] == 1):  
                # for k in range(j,col):  
                #     if(matrix[i][k] == 1):  
                #         n = n + 1  
                if(matrix[i+1][j-1] == 1 or matrix[i+1][j+1] == 1):  
                    n = n + 1;  
  
    print(str(count) + " Non Attacking Pairs : " + str(28 - n))  
    count = count + 1  
    if(28 - n == 27):  
        print("Found " + str(state))  
        sys.exit()  
  
    #Selecting Uphill Successor  
    if(28 - n > 22):  
        initState = state  
  
  
#Main  
generateSuccessor()  
   
