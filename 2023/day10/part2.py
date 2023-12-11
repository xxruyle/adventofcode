from collections import deque

input = open('input.txt')

inputList = []
for i in input:
    inputList.append(i.strip()) 


pathList = [([0] * len(inputList[0])) for i in range(len(inputList))]



inputLen = len(inputList)
lineLen = len(inputList[0])

# [[Norths], [Easts], [Souths], [Wests]]
tiles = {
    "|": [["7", "|", "F"], [], ["L", "|", "J"], []], 
    "-": [[], ["J", "7", "-"], [], ["F", "L", "-"]],
    "L": [["|", "7", "|", "F"], ["-", "J", "7"], [], []],
    "J": [["|", "7", "F"], [], [], ["F", "L", "-"]],
    "7": [[], [], ["|", "J", "L"], ["-", "F", "L"]],
    "F": [[], ["-", "J", "7"], ["|", "L", "J"], []]
}







def checkCorrectInput(i, j):   
    return (i >= 0) and (i < inputLen) and (j >= 0) and (j < lineLen) and inputList[i][j] != "." 



def getNorths(cur, i, j): 
    nearTile = inputList[i][j]
    if cur == "S": 
        return (i, j)
    
    if nearTile in tiles[cur][0]: 
        return (i, j)


def getEasts(cur, i, j): 
    nearTile = inputList[i][j]
    if cur == "S": 
        return (i, j)
    
    if nearTile in tiles[cur][1]: 
        return (i, j)

def getSouths(cur, i, j):
    nearTile = inputList[i][j]
    if cur == "S": 
        return (i, j)
    
    if nearTile in tiles[cur][2]: 
        return (i, j)

def getWests(cur, i, j): 
    nearTile = inputList[i][j]
    if cur == "S": 
        return (i, j)
    
    if nearTile in tiles[cur][3]: 
        return (i, j)



def checkConnection(curTile, i, j):
    nearTile = inputList[i][j]
    if curTile == "S": 
        return (i, j)

    for i in range(4):
        if nearTile in tiles[curTile][i]: 
            return (i, j)
        
    return False 






def checkAdjacency(i, j):  
    connections = []
    cur = inputList[i][j]

    # north                        
    if checkCorrectInput(i-1, j): 
        getConnect = getNorths(cur, i-1, j)
        if getConnect:
            connections.append(getConnect)
             
    # east 
    if checkCorrectInput(i, j+1): 
        getConnect = getEasts(cur, i, j+1)
        if getConnect:
            connections.append(getConnect)
 
    # south 
    if checkCorrectInput(i+1, j): 
        getConnect = getSouths(cur, i+1, j)
        if getConnect:
            connections.append(getConnect)

    # west  
    if checkCorrectInput(i, j-1): 
        getConnect = getWests(cur, i, j-1)
        if getConnect:
            connections.append(getConnect)


    return connections




def getS():
    for i, input in enumerate(inputList):
        for j, letter in enumerate(input):
            if letter == "S":  
                return (i, j)

cord = getS()    

def getSPipe():
    for i in tiles: 
        test = list(inputList[cord[0]]) 
        test[cord[1]] = i
        inputList[cord[0]] = ''.join(test)
        connections = checkAdjacency(cord[0], cord[1]) 

        if len(connections) == 2: 
            return i 
        
        

def printPath():
    for x, i in enumerate(pathList):
        for y, j in enumerate(i):
            if j == 0: 
                print(".", end=" ")
            elif j == "I": 
                print('yes')
                print("\033[96m" + inputList[x][y], end="\033[0m ")
            else: 
                print("\033[31m" + inputList[x][y], end="\033[0m ")
        print("\n")
    print("------\n")



        
visited = set() 

def bfs():
    getSPipe()
    fringe = deque([cord])
    distances = {}
    distances[cord] = 0
    pathList[cord[0]][cord[1]] = 0
    visited.add(cord)
    while fringe: 
        tile = fringe.popleft()
        
        connects = checkAdjacency(tile[0], tile[1])
        
        if connects: 
            for i in connects: 
                if i not in visited: 
                    fringe.append(i) 
                    distances[i] = distances[tile] + 1
                    visited.add(i)
                    pathList[i[0]][i[1]] = distances[i] 


    return max(distances.values())

def getFirstDot(): 
    for i, row in enumerate(inputList):
        for j, tile in enumerate(row):
            if tile == ".": 
                return (i,j)
            

        
def isInsideMap(i, j): 
    return (i >= 0) and (i < inputLen) and (j >= 0) and (j < lineLen)


def insideNorth(i, j): 
    if isInsideMap(i-1, j-1): 
        if inputList[i-1][j-1] == ".": 
            return False
    else: 
        return False 

    

    if isInsideMap(i-1, j):
        if inputList[i-1][j-1] == ".": 
            return False
    else: 
        return False 

    if isInsideMap(i-1, j+1): 
        if inputList[i-1][j-1] == ".":
            return False 
    else: 
        return False 

    return True

    


def insideEast(i, j): 
    count = 0
    if isInsideMap(i-1, j+1): 
        if inputList[i-1][j+1] == ".": 
            return False 
    else: 
        return False 
    

    if isInsideMap(i, j+1):
        if inputList[i][j+1] == ".": 
            return False 
    else: 
        return False 

    if isInsideMap(i+1, j+1): 
        if inputList[i+1][j+1] == ".": 
            return False
    else: 
        return False 

    return True

def insideSouth(i, j): 
    count = 0
    if isInsideMap(i+1, j+1): 
        if inputList[i+1][j+1] == ".": 
            return False 
    else: 
        return False 
    

    if isInsideMap(i+1, j):
        if inputList[i+1][j] == ".": 
            return False 
    else: 
        return False 

    if isInsideMap(i+1, j-1): 
        if inputList[i+1][j-1] == ".": 
            return False
    else: 
        return False 

    return True



def insideWest(i, j): 
    if isInsideMap(i-1, j-1): 
        if inputList[i-1][j-1] == ".": 
            return False 
    else: 
        return False 
    

    if isInsideMap(i, j-1):
        if inputList[i][j-1] == ".":
            return False 
    else: 
        return False 

    if isInsideMap(i+1, j-1): 
        if inputList[i+1][j-1] == ".":
            return False
    else: 
        return False 

    return True 





def isInside(i, j):
    if insideNorth(i, j) and insideEast(i, j) and insideSouth(i, j) and insideWest(i, j): 
        return True 
    
    return False 
        


dot = getFirstDot()
print(pathList)
def getBinary():
    final = []
    for i in pathList: 
        newRow = []
        for j in i: 
            if j == 0: 
                newRow.append(0)
            else: 
                newRow.append(1)

        final.append(newRow)

    return final 
    


def floodFill(arr, i, j):
    stack = [(i, j)]
    while stack: 
        x, y = stack.pop()

        if x < 0 or x >= len(arr) or y < 0 or y >= len(arr[0]) or arr[x][y] != 0: 
            continue 


        arr[x][y] = 2 
        stack.extend([(x+1, y), (x-1, y), (x, y+1), (x,y-1)])

    return arr 
    

        



    

print(bfs())

for i in pathList: 
    print(i)

floodVisit = getBinary()


    




