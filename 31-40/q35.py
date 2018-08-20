def q35():
    # circular primes, how many are there
    # below 1,000,000
    # Simply generate all the prime numbers 
    # beforehand then do circular shtuff on them
    d = {} # key and value are circular primes
    sieve = [x for x in range(2,50)]
    startIndex = 0
    while startIndex < len(sieve):
        index = startIndex
        if sieve[startIndex] == None:
            startIndex+=1
            continue
        else:
            index += sieve[startIndex]
            while index < len(sieve):
                sieve[index] = None
                index += sieve[startIndex]
            # change the startIndex after the loop
            startIndex += 1
    newArray = []
    for i in range(len(sieve)):
        if sieve[i] == None:
            continue
        else:
            d[sieve[i]] = sieve[i]
    for k in d:
        #now do circular stuff
        splitter = str(k).split()
        p = len(splitter) # modulo
        y = 1
        circleArray = []
        while y <= len(splitter):
            # finish here 
            


q35()