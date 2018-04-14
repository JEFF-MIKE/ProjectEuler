def q29(a,b):
    total = 0
    lst = []
    for x in range(2,a+1):
        for z in range(2,b+1):
            total = (x**z)
            if total not in lst:
                lst.append(total)
            else:
                continue
    return len(lst)

print(q29(5,5))
print(q29(100,100))

