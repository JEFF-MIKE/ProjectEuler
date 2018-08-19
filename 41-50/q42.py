def q42():
    total = 0
    triangleNumbers = [1,3]
    triangle = 1
    for i in range(2,27):
        triangle += i
        triangleNumbers.append(triangle)
    # gonna save below in some other file next time as project
    # euler often has these dumb letter requirement things
    d = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    fileR = open("q42.txt","r")
    splitter = fileR.read().strip("\n").replace('"','').lower().split(",")
    print(splitter)
    for word in splitter:
        word = word.strip("\"")
        #print(word)
        score = 0
        for p in word:
            #print(p)
            score += d[p]
        if score in triangleNumbers:
            total += 1
    print(total)
    print(triangleNumbers)
            

q42()
