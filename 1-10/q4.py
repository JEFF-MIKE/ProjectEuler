def q4():
    # I was so inept at programming wtf
    # 
    lst = []
    for i in range(100,1000):
        for j in range(100,1000):
            lst.append(i*j)
    lst.sort(reverse = True)
    for x in range(len(lst)):
        z = [k for k in str(lst[x])]
        end = len(z) - 1
        start = 0
        while True:
            if z[start] == z[end]:
                start += 1
                end -= 1
                if start == end or end == 0:
                    z = "".join(z)
                    print(z)
                    return z
                continue
            else:
                break

q4()