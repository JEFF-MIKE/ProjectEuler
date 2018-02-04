def problem13():
    # adding giant numbers together
    container = []
    fileR = open("q13.txt","r")
    for line in fileR:
        splitter = line.strip().split()
        container.append(int(splitter[0]))
    result = str(sum(container))
    return result[0:10]
        
print(problem13()) # ezpz

