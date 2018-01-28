'''
def q18():
    total = 0
    index = 0
    container = 0
    fileR = open("q18.txt","r")
    for line in fileR:
        splitter = [int(x) for x in line.strip().split()]
        container.append(splitter)
        if len(splitter) == 1:
            total += splitter[0]
            print(total)
            continue
        if splitter[index] > splitter[index + 1]:
            total += splitter[index]
            print(splitter[index],index)
        else:  
            total += splitter[index+1]
            print(splitter[index+1],index + 1)
            index += 1
    for item in
    fileR.close()
    return total
print(q18())
''' 
#This is a much more difficult question than anticipated. This is not a greedy algorithm.
# This is infact, a dynamic programming question

container = []
#fileR = open("q18.txt","r")
fileR = open("q67.txt","r")
for line in fileR:
    container.append([int(x)for x in line.strip().split()])
fileR.close()
n = len(container[-1]) # this is our biggest line, our value for appending
for s in range(len(container)):
    while len(container[s]) != n:
        container[s].append(0)
def q18():
    u = 1
    for g in range((len(container)-2),-1,-1): # we're going down up in this loop
        #print(g)
        for x in range(len(container[g])-u):
            print(x)
            if container[g+1][x] >  container[g+1][x+1]:
                container[g][x] += container[g+1][x]
            else:
                container[g][x] += container[g+1][x+1]
        u +=1
    return container[0][0]
print(q18())
        



        



