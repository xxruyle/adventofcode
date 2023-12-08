import re 

# getting input 
input = open("input.txt")  

inputList = [] 
for i in input:
    inputList.append(i.strip()) 
 
pattern = re.compile("(\d+)\s(red|green|blue)")

possible_games = {
    "red": 12, 
    "green": 13, 
    "blue": 14
}


def getIds():  
    ids = []

    for index, i in enumerate(inputList):
        splt = i.split(":")

        id = int(splt[0][-1])

        cubes = splt[1].strip()

        semicolon_seperated = cubes.split(";")

        possible_cubes = []  
        cur_cubes = {"id": id, "red": 0, "green": 0, "blue": 0} # the cubes we will be reading in         
        for subset in semicolon_seperated: 
            cubePairs = pattern.findall(subset)   

            for pair in cubePairs:  
                cur_cubes[pair[1]] = max(int(pair[0]), int(cur_cubes[pair[1]]) ) 

        if cur_cubes["red"] <= possible_games["red"] and cur_cubes["green"] <= possible_games["green"] and  cur_cubes["blue"] <= possible_games["blue"]: 
            ids.append(index + 1)   

    return sum(ids) 


def main():
    print(getIds() )

if __name__ == "__main__": 
    main() 
             


