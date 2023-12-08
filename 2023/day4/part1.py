import re 

# getting puzzle input 
input = open('input.txt') 

inputList = [] 
for i in input: 
    inputList.append(i.strip())

def getCards(): 
    cards = [] 
    for i in inputList: 
        cards.append(i.split(':')[1].split('|'))  

    # card number is index + 1 

    newCards = [] 
    for card in cards: 
        newCards.append([card[0].strip(), card[1].strip()])

    return newCards  


cardInputs = getCards() 

pattern = re.compile('\d+')
def sumCards():
    cardSums = [] 
    for i, card in enumerate(cardInputs):
        cardSet = set()   

        normalCards = pattern.findall(card[0])  
        personalCards = pattern.findall(card[1])  

        for j in normalCards:
            cardSet.add(j)   

        cardSum = 0 
        for j in personalCards:  
            if j in cardSet:
                if cardSum == 0: 
                    cardSum = 1 
                else: 
                    cardSum *= 2 

        cardSums.append(cardSum)  

    return sum(cardSums)

print(sumCards())