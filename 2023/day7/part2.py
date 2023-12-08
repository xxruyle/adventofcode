from functools import cmp_to_key 
# getting input 
input = open("input.txt") 

inputList = [] 
for i in input:
    inputList.append(i.strip()) 


hands = []  
bids = [] 
for i in inputList: 
    hands.append(i.split(' ')[0])  
    bids.append(i.split(' ')[1]) 



cardStrength = {"A": 12, "K": 11,  "Q": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1,"J": 0,
}


handType = { 
    "fiveofkind": [],  
    "fourofkind": [], 
    "fullhouse": [], 
    "threeofkind": [],  
    "twopair": [], 
    "onepair": [], 
    "highcard": [],  
} 

bidPair = {} 

def getHandType(purgeList, hand): 
    if not purgeList: 
        handType["highcard"].append(hand)   
        return 

    purgeList = sorted(purgeList)  

    if len(purgeList) == 1: 
        if purgeList[0] == 5: 
            handType["fiveofkind"].append(hand) 
        elif purgeList[0] == 4: 
            handType["fourofkind"].append(hand) 
        elif purgeList[0] == 3: 
            handType["threeofkind"].append(hand) 
        elif purgeList[0] == 2: 
            handType["onepair"].append(hand) 
    elif len(purgeList) == 2:  
        if purgeList[0] == 2 and purgeList[1] == 3: 
            handType["fullhouse"].append(hand) 
        elif purgeList[0] == 2 and purgeList[1] == 2:
            handType["twopair"].append(hand) 


def getMaxCard(cards): 
    curMax = "A" 
    for i in cards: 
        if i != "J": 
            if cards[i] > cards[curMax]: 
                curMax = i   
    return curMax 

def purgeNums():
    for i, hand in enumerate(hands):
        bidPair[hand] = int(bids[i] )

        cards = {
        "A": 0, "K": 0,   "Q": 0, "T": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0, "J": 0
        } 
        for char in hand: 
            cards[char] += 1 

        # part 2 addition 
        maxChar = getMaxCard(cards) 
        cards[maxChar] += cards["J"] 
        cards["J"] = 0

        nums = [] 
        for i in cards: 
            if cards[i] != 0: 
                nums.append(cards[i]) 


        numsPurge = [] 
        for i in nums: 
            if i != 1: 
                numsPurge.append(i) 

        numsPurge = sorted(numsPurge)  

        getHandType(numsPurge, hand) 


def compareHands(a, b): 
    for i in range(5):  
        if a[i] != b[i]: 
            if cardStrength[a[i]] > cardStrength[b[i]]:  
                return 1 
            elif cardStrength[a[i]] < cardStrength[b[i]]:  
                return -1 
            
    return 0  

                
def getRanks():
    purgeNums() 

    ranks = [[] for i in range(len(hands))] 
     
    count = 0   
    for i in reversed(handType):  
        if handType[i]:  
            count += 1  
     
            for j in handType[i]:  
                ranks[count].append(j)  

    for i, r in enumerate(ranks): 
        if r: 
            ranks[i] = sorted(r, key=cmp_to_key(compareHands)) 

    products = []  
    rankCount = 1 
    for i, r in enumerate(ranks):   
        for j in r: 
            products.append(rankCount * bidPair[j])   
            rankCount += 1  

    return sum(products)


def main():
    print(getRanks())

if __name__ == "__main__":
    main() 

    
    
    

