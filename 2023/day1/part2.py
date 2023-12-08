import re 

# getting input 
input = open("input.txt") 

inputList = [] 
for i in input:
    inputList.append(i.strip()) 


# pattern matching
pattern = re.compile("(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
convertDigit = {
    "one": '1', 
    "two": '2',
    "three": '3', 
    "four": '4', 
    "five": '5', 
    "six": '6',
    "seven": '7', 
    "eight": '8', 
    "nine": '9' 
}

# answering  
def getSum():
    sum = 0 
    for i in inputList:  
        get = pattern.findall(i)   
        new = [get[0], get[-1]] 
     
        construct = ""  
        for j in new:  
            if j.isdigit():  
                construct += j  
            elif j in convertDigit:  
                construct += convertDigit[j]   
           
        sum += int(construct) 
     
    return sum  


def main(): 
    print(getSum() )

if __name__ == "__main__": 
    main() 
    

