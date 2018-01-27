def problem10():
    total = 0
    a = 2
    i = 3
    while (i < 2000000):
        if i == a:
            a = 2
            total += i
            i += 1
        if i % a == 0:
            a = 2
            i += 1
        a += 1
    return total
# print(problem10()) # this is correct, but extremely inefficient it appears
def problem10i():
    total = 0
    lst = [2]
    i = 3
    while i < 2000000:
        counter = 0
        for item in lst:
            if i % item == 0:
                break
        else:
            lst.append(i)
            i += 1
        i += 1
    return sum(lst)

# print(problem10i()) Isn't wrong and is still an improvement, but still too slow

# Need the sieve of eratostenes for this (Sieve is an ancient algorithm)

def Sieve(n):
    sieve = [x for x in range(2,n)] # not n + 1 because below n
    index = 0 # start off at 2
    length = len(sieve)
    total = 0
    while index < length:
        g = index
        if sieve[g] != None:
            total += sieve[g]
            g += sieve[index]
            while g < len(sieve):
                sieve[g] = None
                g += sieve[index]
            index += 1
        else:
            index += 1
    return total

print(Sieve(2000000)) # This is correct, and takes very little time
    
            
