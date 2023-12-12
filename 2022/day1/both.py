input = open("input.txt").read()
input = input.split("\n")

def getCalories():
    calories = []
    newList = []   
    for i in input: 
        if i != "": 
            newList.append(int(i))
        else: 
            calories.append(newList)
            newList = [] 
    calories.append(newList)  

    calorieSums = sorted([sum(x) for x in calories])  

    return calorieSums 


def main(): 
    calorieSums = getCalories() 
    print(max(calorieSums))
    topThree = [calorieSums[-x] for x in range(1,4)] 

    print("Part 1: ", max(calorieSums))
    print("Part 2: ", sum(topThree))


if __name__ == "__main__": 
    main()    