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
                    
