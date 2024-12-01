
def readinput(): 
    left = []
    right = []

    file = open('input.txt', 'r')  
    for line in file: 
        l, r = line.strip().split("   ")

        left.append(l)
        right.append(r)

    file.close()
    return left, right


def part1(): 
    left, right = readinput()
    left.sort()
    right.sort()
    count = 0

    for i, num in enumerate(left):
        l = int(num)
        r = int(right[i])
        count += abs(r - l)

    return count

def part2(): 
    left, right = readinput()
    dic = {}
    for num in right: 
        n = int(num)
        if n in dic: 
            dic[n] += 1 
        else: 
            dic[n] = 1 

    count = 0 
    for num in left: 
        n = int(num)
        if n not in dic: 
            pass
        else: 
            count += n*dic[n]

    return count


def main(): 
    # part1()
    print(part2())

if __name__ == "__main__": 
    main()
