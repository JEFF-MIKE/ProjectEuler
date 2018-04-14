def q28(x):
    # calculate the diagonals of a spiral
    # without generating the actual spiral
    m = x**2 # max value of diagonal
    lst = [x for x in range(1,m+1)] # want to include m
    shift = 1 # always shift to the right
    r,d,u,p = 2,1,2,2 # p is left
    total = 1
    i = 0 # index
    while (i) <= len(lst):
        i += shift
        i += d
        if i >= len(lst):
            return total
        total += lst[i]
        i += p
        if i >= len(lst):
            return total
        total += lst[i]
        i += u
        if i >= len(lst):
            return total
        total += lst[i]
        i += r
        if i >= len(lst):
            return total
        total += lst[i]
        r += 2
        d += 2
        u += 2
        p += 2
        if r >= len(lst)-1:
            return total
    return total


print(q28(5))
print(q28(1001))



