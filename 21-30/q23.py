def abundant(x):
    # if the sum of the numbers factors is greater than number "n",
    # return the abundant number, otherwise return zero
    result = 0
    for a in range(1,(x//2+1)):
        if x % a == 0:
            result += a
    if result > x:
        return result
    else:
        return 0


def q23():
    # returns the sum of all numbers that are not the sum of two
    # abundant numbers
    sieve = [g for g in range(28124)]
    abunNum = []
    for n in range(len(sieve)):
        result = abundant(sieve[n])
        if result == 0 or result > 28123: # all numbers greater than 28124 are the sum of abundant numbers
            continue
        #print(result)
        abunNum.append(result)

    return abunNum

print(abundant(12))
print(abundant(11))
print(abundant(28))

print(q23())