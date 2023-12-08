# getting input 
input = open("input.txt") 

inputList = [] 
for i in input:
    inputList.append(i.strip()) 


# answering 

def getSum():   
    sum = 0  

    for i in inputList: 
        digits = []  
        for c in i: 
            if c.isdigit():
                digits.append(c) 

        digit = int(f"{digits[0]}{digits[-1]}") 
        sum += digit 

    return sum 

def main(): 
    print(getSum() )

if __name__ == "__main__": 
    main() 

    

