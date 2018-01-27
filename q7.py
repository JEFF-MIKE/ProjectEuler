def problem7():
    a = 2 # This will be our factor
    b = 2 # the number we are trying to deduct is prime or not
    counter = 0
    while True:
        if b == a: # it is prime in this case:
            counter += 1
            if counter == 10001:
                break
            b += 1
            a = 2
            continue 
        if b % a == 0:
            # not prime,reset
            b += 1
            a = 2
            continue
        a += 1
    return b

print(problem7())
        
            
