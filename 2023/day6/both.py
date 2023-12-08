import re  
from math import prod, pow, sqrt, floor, ceil
# getting input 
input = open("input.txt") 

inputList = [] 
for i in input:
    inputList.append(i.strip()) 

digits = re.compile('\d+') 

timeDistance = [] 
for i in inputList: 
    timeDistance.append([eval(x) for x in digits.findall(i)]) 

timeDistanceKerning = [] 

for i in inputList:
    timeDistanceKerning.append(int(''.join(digits.findall(i)))    )




def countWays():  
    counts = []  
    for x, d in enumerate(timeDistance[0]): 
        count = 0 
        for i in range(d + 1):  
            record = timeDistance[1][x]    
            distance = (d-i) * i     
            if distance > record: 
                count += 1 

        counts.append(count)

    return prod(counts) 

def countKerningWays():
    count = 0 
    d = timeDistanceKerning[0] 
    for i in range(d + 1):   
        record = timeDistanceKerning[1]     
        distance = (d-i) * i     
        if distance > record: 
            count += 1 


    return count


def quadraticWays():
    counts = []  
    for x, d in enumerate(timeDistance[0]):  
        record = timeDistance[1][x]  
        low =  floor(( -d  +  sqrt( pow(d,2) - 4*(-1)*(-record) ))   / -2)    # -distance + sqrt(d^2 - 4(-1)(-record)) / 2(-1)  
        high = ceil((-d  -  sqrt( pow(d,2) - 4*(-1)*(-record) ))   / -2)  -1       
        counts.append(high - low) 

    return prod(counts)

def quadraticKerningWays():
    distance = timeDistanceKerning[0] 
    record = timeDistanceKerning[1] 
    low =  floor(( -distance  +  sqrt( pow(distance,2) + 4*(-record) ))   / -2)    
    high = ceil( (-distance  -  sqrt( pow(distance,2) + 4*(-record)  ))   / -2)  - 1         
    
    return high - low 



def main(): 
    print("Part1: ", quadraticWays())    
    print("Part2: ", quadraticKerningWays())  

if __name__ == "__main__":
    main() 


        




