import time
def problem11():
    # largest number from a block of numbers
    container = []
    maxa = 0
    fileR = open("q11.txt","r")
    for line in fileR:
        splitter = line.strip().split()
        maxi = max(splitter)
        #print(maxi)
        #print(splitter.index(maxi))
        container.append([int(x) for x in splitter])
    start = time.time()
    for i in range(len(container)):
        for g in range(len(container[i])-3):
            #print(container[i][g])
            current = container[i][g] * container[i][g + 1] * container[i][g + 2] * container[i][g +3]
            if  current > maxa:
                maxa = current
    # across done, now for above and below
    for m in range(len(container) - 3):
        for a in range(len(container[m])):
            #print(container[m][a])
            current = container[m][a] * container[m + 1][a] * container[m + 2][a] * container[m + 3][a]
            if current > maxa:
                maxa = current
    # above and below done, now for the fun part (Diagonals)
    # gonna start with diagonals facing to the right first
    for k in range(len(container)-3):
        for x in range(len(container[k]) - 3):
            current = container[k][x] * container[k + 1][x + 1] * container[k +2][x + 2] * container[k + 3][x + 3]
            if current > maxa:
                maxa = current
    for p in range(len(container)-3): # this is our grid navigation
        for q in range(3,len(container)):
            current = container[p][q] * container[p+1][q-1] * container[p+2][q-2] * container[p+3][q-3]
            if current > maxa:
                maxa = current
    print(time.time() - start)
    return maxa       
print(problem11()) # this is correct
