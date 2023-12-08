import re   
from math import prod, pow, sqrt, floor, ceil, lcm
# getting input 
input = open("input.txt") 

inputList = [] 
for i in input:  
    inputList.append(i.strip())   



graph  = {}   # the actual graph representation of the input 

instructions = inputList.pop(0) 
pattern = re.compile('\w+') 

for i in inputList[1:]: 
    if i != '': 
        nodes = pattern.findall(i)  
        graph[nodes[0]] = [nodes[1], nodes[2]] 

nodes = list(graph) 

def traverse(): 
    '''Fort part1'''
    cur = "AAA"  # start at first node in example it is "AAA"  
    count = 0
    while cur != "ZZZ":    
        curInstruction = instructions[count % len(instructions)]  # for looping instructions  
        if curInstruction == "L": 
            cur = graph[cur][0]   
        elif curInstruction == "R": 
            cur = graph[cur][1] 

        count += 1 
    return count 
 

def ghostTraverse():  
    '''For part2'''
    curs =  [x for x in nodes if x[-1] == "A"]  # start with As 

    count = 0
    elements = []  # number elements to get the LCM of 
    while len(elements) < len(curs):   
        curInstruction = instructions[count % len(instructions)] # for looping instructions
        for i, c in enumerate(curs):    
            # do not continue looping the cur node if it is already at the end 
            if c[-1] == "Z":  
                continue 

            if curInstruction == "L": 
                curs[i] = graph[c][0] 
            elif curInstruction == "R":
                curs[i] = graph[c][1] 

            # if it arrives at a Z end node then we add the current count to the elements 
            if curs[i][-1] == "Z": 
                elements.append(count+1)
        count += 1 

    """
    once all the nodes found an end Z node we just take the LCM
    to find how many cycles it would take for them all to converge  
    at the same time 
    """ 
    return lcm(*elements) 

def main(): 
    print(traverse()) 
    print(ghostTraverse())

if __name__ == "__main__": 
    main()








