from collections import deque
import heapq

input = open('input.txt')

inputList = []
for i in input: 
    inputList.append(list(i.strip()))

def printMap():
    for i in inputList: 
        print(i)


inputLen = len(inputList)
rowLen = len(inputList[0])




largeRows = []
largeCols = []
def expandGalaxies(): 
    for i, input in enumerate(inputList):
        if "#" not in input: 
            largeRows.append(i)
            

    for i in range(len(inputList[0])):
        col = []
        for j in range(len(inputList)): 
            col.append(inputList[j][i])

        if "#" not in col: 
            largeCols.append(i)
expandGalaxies()
            

    

def getGalaxies(): 
    galaxies = []
    for i, row in enumerate(inputList):
        for j, node in enumerate(row):
            if node == "#": 
                galaxies.append((i, j))

    return galaxies 



def manhattanDistance(start, end, expansion): 
    x1 = start[1]
    x2 = end[1]

    y1 = start[0]
    y2 = end[0]

    dist = 0 

    if x1 > x2: 
        x2, x1 = x1, x2

    xs = range(x1+1, x2+1)  

    for x in xs: 
        if x in largeCols: 
            dist += expansion 
        else: 
            dist += 1 

    ys = range(y1+1, y2+1) 
    for y in ys: 
        if y in largeRows: 
            dist += expansion 
        else: 
            dist += 1 
    
    return dist 



def getGalaxySum(expansion):



    galaxies = getGalaxies()
    gs = {}
    visitedSet = set()
    for x, i in enumerate(galaxies):
        gs[x+1] = []
        for y, j in enumerate(galaxies):
            if j != i and ((x+1,y+1) not in visitedSet and (y+1,x+1) not in visitedSet): 
                visitedSet.add((x+1, y+1))
                dist = manhattanDistance((i[0], i[1]), (j[0], j[1]), expansion)
                gs[x+1].append(dist)

    vals = list(gs.values())
    valSum = 0 
    for i in vals: 
        valSum += sum(i)
    return valSum 



def main(): 
    expansion1 = 2 # for part 1 
    expansion2 = 1000000 # for part 2  

    print("Part 1: ", getGalaxySum(expansion1))
    print("Part 2: ", getGalaxySum(expansion2))

if __name__ == "__main__":
    main()


    


