def q30():
    # Much simpler than what I initially thought.
    # just record the power of 5 for each number in a dictionary
    # then just access it over the loop per number
    answer_list = []
    d = dict()
    for i in range(10):
        d[i] = i ** 5
    for x in range(10,1000000):
        z = [int(y) for y in str(x)] #Disgusting but it it works
        for c in range(len(z)):
            z[c] = d[z[c]]
        u = sum(z)
        if u == x:
            answer_list.append(u)
    print(answer_list)
    print(sum(answer_list))

q30()

