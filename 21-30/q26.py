from math import modf
def unitFraction(number):
    greatest = 0
    # gets the longest recurring decimal
    # in the range of d, doing the p/q test
    print((10**(17-1)-1)//17)
    for i in range(2,number):
        p = len(str((10**(i-1)-1)//i))
        if p > greatest:
            #print(p)
            greatest = p
    return greatest

print(unitFraction(1000))

def test2(z):
    #another attempt at the question
    b = 10 # decimal base
    sieve = [x for x in range(b,z)]
    for o in range(len(sieve)):
        isPrime = True
        if sieve[o] == None:
            continue
        for q in range(3,sieve[o]):
            if sieve[o] % q != 0:
                continue
            else:
                isPrime = False
                break
        if isPrime:
            prime = sieve[o] # actual number
            #print(prime, 'is prime!')
            for i in range(o+prime,len(sieve),prime ):
                sieve[i] = None
    #sieve now generated.
    #time to do Fermats equation
    t = 0
    r = 1
    n = 0
    for a in range(len(sieve)):
        if sieve[a] == None:
            continue 
        else:
            t = t+1
            x = r * b
            d = x / sieve[a]
            r = x % sieve[a]
            n = n * b + d
            if r != 1:
                continue
            if t == p - 1:
                print(n)    
test2(1000)



