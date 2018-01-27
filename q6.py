def problem6(n):
    square = 0 # sum of square
    sumsquare = 0 # square of the sum
    for g in range(1,n+1):
        square += g**2
        sumsquare += g
    sumsquare = sumsquare ** 2
    return sumsquare - square

print(problem6(10))
print(problem6(100))
