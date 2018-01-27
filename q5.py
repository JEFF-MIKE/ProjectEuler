def problem5():
    a = 2520 # Number we are dividing
    b = 20 # Number by which we are dividing by
    while True:
        if b != 0:
            if a % b == 0:
                b -= 1
                continue
        if b == 0:
            break
        b = 20
        a += 20
    return a

print(problem5())
            
