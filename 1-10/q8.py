def problem8():
    container = []
    # find the largest product of 13 adjacent digits
    numberLst = []
    fileR = open("q8.txt","r").read()
    for line in fileR:
        splitter = line.strip().split()
        for item in splitter:
            container.append(int(item))
    start = 0
    end = 12 # start and end are indexes
    while end < (1000):
        number = container[start]
        for g in range((start+1),(end+1)):
            number *= container[g]
        numberLst.append(number)
        start += 1
        end +=1
    return max(numberLst)
        

print(problem8())
