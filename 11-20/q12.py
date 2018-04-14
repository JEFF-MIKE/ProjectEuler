'''
def problem12():
    # First triangular number with 500 divisibles
    triangle = 3 # our triangular number
    adder = 3 # How much we add by each round
    while True:
        lst = []
        lst.append(triangle)
        for i in range(2,triangle + 1):
            if triangle % i == 0:
                number = triangle
                while number % i == 0:
                    number //= i
                    if number not in lst:
                        lst.append(number)
        print(len(lst))
        if len(lst) > 500:
            break
        triangle += adder
        adder += 1
    return triangle

print(problem12())
'''
def q12():
    # alright second attempt at this in April now
    # wtf was I smoking back when I first did this, this is 
    # so easy
    lst = [] # beginning triangular number list
    total = 1
    t = 1
    while True:
        factorCounter = 2 # all numbers can be divided by themselves and 1
        t += 1
        total += t
        x = total
        for i in range(2,(x//2)+1):
            if x % i == 0:
                factorCounter += 1
        if factorCounter > 500:
            return x

print(q12())