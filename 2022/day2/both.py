input = open("input.txt")
inputList = [(i.strip().split(' ')[0], i.strip().split(' ')[1]) for i in input]

pairs = { 
    "A": "X", 
    "B": "Y", 
    "C": "Z"
}


wins = {
    "A": "Y", # Rock: paper 
    "B": "Z",# Paper: scissors 
    "C": "X" # scissors:  rock
}


losses = { 
    "A": "Z", # Rock: paper 
    "B": "X",# Paper: scissors 
    "C": "Y" # scissors:  rock
}


scores = {
    "X": 1, # rock 
    "Y": 2, # paper 
    "Z": 3 # scissors 
}


def getPart1Score():
    totalScore = 0
    for pair in inputList: 
        if wins[pair[0]] == pair[1]: # if we win 
            totalScore += scores[pair[1]] + 6  
        elif pairs[pair[0]] == pair[1]: # if we draw 
            totalScore += scores[pair[1]] + 3  
        else: # if we lose 
            totalScore += scores[pair[1]]

    return totalScore 


def getPart2Score(): 
    totalScore = 0
    for pair in inputList: 
        if pair[1] == "X": # lose 
            totalScore += scores[losses[pair[0]]] 
        elif pair[1] == "Y": # draw 
            totalScore += scores[pairs[pair[0]]] + 3 
        elif pair[1] == "Z": # win 
            totalScore += scores[wins[pair[0]]] + 6 

    return totalScore 
        

def main(): 
    print("Part 1: ", getPart1Score())
    print("Part 2: ", getPart2Score())

if __name__ == "__main__": 
    main()