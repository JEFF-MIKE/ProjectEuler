import time
# The longest collatz sequence. The answer must end at 1.
def problem14(n):
    # a collatz sequence with the following properties :
    # If  n is even, n/2
    # If n is odd, 3(n) + 1
    number = 0
    lstA = []
    lstB = []
    start = time.time()
    for i in range(1,n-1,2):
        number = i
        counter = 0
        while True:
            if number == 1:
                break
            if number % 2 == 0:
                number = number / 2
                counter += 1
                continue
            if number % 2 == 1:
                number = ((number * 3)+1)
                counter += 1
                continue
        lstA.append(i)
        lstB.append(counter)
    maxa = max(lstB) # the number with the highest counter
    index = lstB.index(maxa)
    r = lstA[index]
    end = time.time() - start
    return "Highest Counter: %s\nNumber: %s\nTime taken:%s" % (maxa,r,end)
print(problem14(1000000)) # correct, but takes awhile
# god-tier advice: do not run the max(built-in) function on a python dictionary
# max() of a string becomes ugly 
