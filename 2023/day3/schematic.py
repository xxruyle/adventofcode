import re 

# getting input 
input = open("./input.txt") 

inputList = [] 
for i in input:
    inputList.append(i.strip()) 

inputLen = len(inputList)  
lineLen =  len(inputList[0]) 

def checkCorrectInput(i, j):   
    return i >= 0 and i < inputLen and j >= 0 and j < lineLen   

def checkSymbol(i, j): 
    return inputList[i][j] != "." and not inputList[i][j].isdigit()    

def checkAdjacency(i, j):  
    # up                        
    if checkCorrectInput(i-1, j): 
        if checkSymbol(i-1, j): 
            return True 
             
    # right 
    if checkCorrectInput(i, j+1): 
        if checkSymbol(i, j+1): 
            return True 
 
    #left 
    if checkCorrectInput(i, j-1): 
        if checkSymbol(i, j-1): 
            return True 

    #down  
    if checkCorrectInput(i+1, j): 
        if checkSymbol(i+1, j):
            return True 

    # diagonal up right 
    if checkCorrectInput(i-1, j+1): 
        if checkSymbol(i-1, j+1):
            return True 

    # diagonal up left 
    if checkCorrectInput(i-1, j-1): 
        if checkSymbol(i-1, j-1):
            return True 


    # diagonal down right 
    if checkCorrectInput(i+1, j+1): 
        if checkSymbol(i+1, j+1):
            return True 

    # diagonal down left 
    if checkCorrectInput(i+1, j-1): 
        if checkSymbol(i+1, j-1): 
            return True

pattern = re.compile('\d+')
def checkSymbols():
    sums = 0 

    for i, line in enumerate(inputList): # loop through every line in the input list 
        numbers = pattern.findall(line) 

        f = 0 # keeps track of numbers regex index
        inDigit = False    
        found = False # if we found an adjacent symbol 
        j = 0
        while j < lineLen:
            found = False 
            if inputList[i][j].isdigit():  
                inDigit = True 
                if checkAdjacency(i, j):
                    # print(numbers, inputList[i][j], f)
                    sums += int(numbers[f]) 
                    found = True 
                    while j < lineLen: 
                        if inputList[i][j].isdigit():
                           j += 1 
                        else: 
                            break  
            else: 
                if inDigit:  
                    f += 1   
                    inDigit = False  

            if not found:    
                j += 1 

    return sums 



print(checkSymbols()) 

