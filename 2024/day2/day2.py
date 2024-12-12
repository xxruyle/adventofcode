
def readinput(): 
    file = open('input.txt', 'r')  
    out = []
    for line in file: 
        out.append(line.strip().split(" " ))

    file.close()
    return out 



def part1(): 
    inp = readinput()
    unsafe_count = 0 
    for level in inp: 
        decreasing = False 
        increasing = False 
        prev = int(level[0])
        first = int(level[1]) 
        if first - prev < 0: 
            increasing = False 
            decreasing = True
        else: 
            increasing = True
            decreasing = False 
            

        for n in range(1, len(level)): 
            num = int(level[n])
            absdiff = abs(prev - num) 
            diff = prev - num 
            if decreasing and diff <= 0: 
                unsafe_count += 1 
                break 

            if increasing and diff >= 0: 
                unsafe_count += 1 
                break


            if absdiff > 3 or absdiff < 0:
                unsafe_count += 1 
                break

            prev = num 

    return len(inp) - unsafe_count

def part2(): 
    inp = readinput()



def main(): 
    print("Part 1: ", part1()) 

if __name__ == "__main__": 
    main()
