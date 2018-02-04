def q16():
    # returns the sum of digits
    a = 2
    b = 1000
    # We're gonna exploit the fact that 2**500 * 2**500 == 2**1000
    # break it down basically
    splitter = [int(x) for x in str(a**b)]
    return sum(splitter)

print(q16())