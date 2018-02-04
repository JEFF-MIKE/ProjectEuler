def q21(n):
    # amicable numbers
    lst = []
    for i in range(10000):
        result1 = d(i)
        result2 = d(result1)
        if result1 == result2:
            continue # ignore, not a PAIR
        if result2 == i:
            if i not in lst:
                lst.append(i)
            if result1 not in lst:
                lst.append(result1)
    print(lst)
    return sum(lst)


def d(n):
    # exactly as it is in the project euler
    if n ==1 or n == 0:
        return 0
    result = 0
    a = 2
    gen = (x for x in range(1,n//2+1))
    for item in gen:
        if n % item == 0:
            result += item
    return result
print(d(220)) 
print(d(284))
print(d(496))
print(d(8128))
print(d(28))
print(q21(10000))
            
