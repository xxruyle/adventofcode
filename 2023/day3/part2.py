import re
from math import prod 

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
    # return inputList[i][j] != "." and not inputList[i][j].isdigit()    
    if inputList[i][j] == "*": 
        return (i,j)


def checkAdjacency(i, j):  
    # up                        
    if checkCorrectInput(i-1, j): 
        res = checkSymbol(i-1, j)
        if res: 
            return res 
             
    # right 
    if checkCorrectInput(i, j+1): 
        res =  checkSymbol(i, j+1) 
        if res: 
            return res 

 
    #left 
    if checkCorrectInput(i, j-1): 
        res =  checkSymbol(i, j-1)
        if res: 
            return res 

    #down  
    if checkCorrectInput(i+1, j): 
        res = checkSymbol(i+1, j)
        if res: 
            return res 

    # diagonal up right 
    if checkCorrectInput(i-1, j+1): 
        res = checkSymbol(i-1, j+1) 
        if res: 
            return res 

 
    # diagonal up left 
    if checkCorrectInput(i-1, j-1): 
        res = checkSymbol(i-1, j-1) 
        if res: 
            return res 


    # diagonal down right 
    if checkCorrectInput(i+1, j+1): 
        res = checkSymbol(i+1, j+1)
        if res: 
            return res 

    # diagonal down left 
    if checkCorrectInput(i+1, j-1): 
        res = checkSymbol(i+1, j-1)
        if res: 
            return res 


pattern = re.compile('\d+')
sumsAndTuple = [] 
def checkSymbols(): 
    symbolSum = 0 
    for i, line in enumerate(inputList): # loop through every line in the input list 
        numbers = pattern.findall(line) 

        f = 0 # keeps track of numbers regex index
        inDigit = False    # if we are in a digit currently  
        found = False # if we found an adjacent symbol 
        j = 0
        while j < lineLen:
            found = False 
            if inputList[i][j].isdigit():  
                inDigit = True 
                res = checkAdjacency(i, j)
                if res:
                    sumsAndTuple.append((int(numbers[f]), res))  

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

 


def getGears():
    gearDict = {}     
    for i in sumsAndTuple: 
        if i[1] not in gearDict:  
            gearDict[i[1]] = [i[0]]
        else: 
            gearDict[i[1]].append(i[0])


    gearProducts = []
    for i in gearDict: 
        if len(gearDict[i]) > 1: 
            gearProducts.append(prod(gearDict[i]))

    return sum(gearProducts)  


def main():
    checkSymbols() 
    print(getGears() )

if __name__ == "__main__": 
    main() 



