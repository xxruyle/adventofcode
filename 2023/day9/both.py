# getting input 
input = open('input.txt') 

inputList = [i.strip() for i in input]  

sequences = [] 
for i in inputList: 
    new = []  
    for x in i.split(' '): 
        new.append(int(x))
    sequences.append(new)    

def allZeros(differences):  
    for i in differences: 
        if i != 0: 
            return False 
    return True  

def getHistory(diff):
    '''For part 1'''
    sums = [0] 
    for i in range(len(diff) - 1, -1, -1): 
        sums.append(diff[i][-1] + sums[-1]) 
    return sums[1:]     

def getHistoryBackwards(bHistory):      
    '''For part 2'''
    fronts = [x[0] for x in bHistory]        
    diffs = [0]
    for i in range(len(fronts) - 1, -1, -1): 
        diffs.append(fronts[i] - diffs[-1]) 

    return diffs[-1]


def getHistories(): 
    histories = []   
    backwardsHistories = []

    for s in sequences: 
        differences = [s]   
        prev = differences[-1]  
        while not allZeros(prev): 
            new = [prev[j+1] - prev[j] for j in range(len(prev) - 1)]                 
            differences.append(new)  
            prev = differences[-1]  

        # for part 1 
        history = getHistory(differences) 
        histories.append(history[-1]) 

        # for part 2 
        backwardsHistories.append(getHistoryBackwards(differences) )

    return sum(histories), sum(backwardsHistories)

def main():
    answer = getHistories()
    print("Part 1: ", answer[0])
    print("Part 2: ", answer[1])

    
if __name__ == "__main__":
    main()