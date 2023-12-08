import re 
from math import inf

# getting puzzle input 
input = open('test.txt').read().strip() 

newline = re.compile('(?<=\n)\n')  
digits = re.compile('\d+') 
inputList = newline.split(input)

seedInfo = []  
for i in inputList: 
    seedInfo.append(digits.findall(i))  

# seeds 
seeds = seedInfo[0] 

# maps 
seedsoil = seedInfo[1] 
soilfert = seedInfo[2]  
fertwater = seedInfo[3]    
waterlight = seedInfo[4] 
lighttemp = seedInfo[5] 
temphumidity = seedInfo[6] 
humiditylocation = seedInfo[7] 

seedMaps = [
    seedsoil, soilfert, fertwater, waterlight, lighttemp, temphumidity, humiditylocation 
]

def toMatrix(cList): 
    lines = len(cList) // 3 # number of lines in map   
    maps = []  
    start = 0  
    end = 3 
    for i in range(lines):   
        maps.append([eval(x) for x in cList[start:end]])  
        start += 3 
        end += 3
    return maps 

def convertSeed(num, toConvertList):  
    '''the num we want to convert and the list with the information to convert''' 
    toConvertList = toMatrix(toConvertList) 
    ranges = []    
    for m in toConvertList:  
        x = (m[0], m[0] + m[2] - 1)
        y = (m[1], m[1] + m[2] - 1)

        ranges.append([x,y])

    cur = [] 
    for r in ranges:   
        # just want to check the second tuple value since that is the seed value info 
        seedRange = r[1]  
        if num >= seedRange[0] and num <= seedRange[1]: 
            cur = r   
    if not cur: 
        return num 

    sourceLowerBound = cur[1][0]          
    destLowerBound = cur[0][0] 

    conversion = destLowerBound + (num - sourceLowerBound)     
    return conversion 


# for part 1 
def mapConvertMin():
    allCurs = []  
    for seed in seeds: 
        cur = int(seed)
        for conv in seedMaps:  
            cur = convertSeed(cur, conv)  
        allCurs.append(cur)
    return min(allCurs)

# for part 2  
def getSeedRanges(): 
    seedRanges = []  
    seedPairs = len(seeds) // 2  
    start = 0 
    end = 2 
    for i in range(seedPairs):
        seedRanges.append(tuple([eval(x) for x in seeds[start:end]]))   
        start += 2 
        end += 2 

    seedTuples = [] 
    for i in seedRanges: 
        seedTuples.append([i[0], i[0] + i[1]])  

    return seedTuples


# 82 wrong  
def mapConvertRangeMin():   
    ranges = getSeedRanges() 
    print(ranges) 
    for r in ranges:   
        cur = r[0]  
        for seed in seedMaps:  
            cur = convertSeed(cur, seed)  
        r[0] = cur  
        cur = r[1]  
        for seed in seedMaps:  
            cur = convertSeed(cur, seed)  
        r[1] = cur    

    print(ranges) 

                    

    

        



# mapConvertRangeMin()
                          


