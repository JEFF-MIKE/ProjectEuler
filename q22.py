def q22():
    # reads in q22.txt and calculates the score of it
    fileR = open("q22.txt","r")
    string = fileR.read()
    fileR.close()
    d = {"\"":0,"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    result = 0
    factor = 1
    temp = 0
    string = string.split(',')
    string = sorted(string)
    print(string[937])
    for item in string:
        if item == "\'":
            continue
        elif item == "\"":
            continue
        else:
            for letter in item:
                  temp += d[letter]
        result += (temp * factor)
        factor += 1
        temp = 0
    return result

print(q22())