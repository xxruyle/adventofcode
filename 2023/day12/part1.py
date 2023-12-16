input = open('input.txt') 

inputList = [] 
for i in input: 
    inputList.append(i.strip())

print(inputList) 


vals = [] 
for i in range(len(inputList)): 
    splt = inputList[i].split(' ') 
    conditions = list(splt[0])
    nums = [eval(x) for x in splt[1].split(',')]

    vals.append((conditions, nums))


test = vals[0] 

springInfo = test[0]
size = test[1] 

print(springInfo, size)

