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
                cardSum += 1 

        cardSums.append(cardSum)  

    return cardSums

counting = sumCards()  # get "counting sort" like array 
countDict = {}  
cardCount = {k:1 for k in range(1, len(counting) + 1)}   # list of copies per card  
def countSums(): 
    for i, c in enumerate(counting):
        curCard = i + 1 

        for j in range(cardCount[curCard]):
            for k in range(curCard+1, c+curCard+1): 
                cardCount[k] += 1 

countSums()
print(sum(cardCount.values())) 











    








