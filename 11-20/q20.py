from math import factorial
def factorialSum(n):
    # returns the sum of the digits of the factorial of n
    result = [int(x) for x in str(factorial(n))]
    return sum(result)
print(factorialSum(100))
print(factorialSum(10))