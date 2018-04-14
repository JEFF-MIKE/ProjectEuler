import math

def q25():
    # find the fibonacci number with 1000 digits
    fib = [1,1]
    i = 1 # the nth number
   # print(fib[i-1]+fib[i])
    while True:
        x = fib[i-1] + fib[i]
        g = str(x)
        if len(g) == 1000:
            print(len(str(fib[5])))
            print(len(str(fib[6])))
            print(len(str(fib[4779])))
            print(len(str(fib[4780])))
            return (i + 2) # I add 2 here to make up for the i += 1 below
        fib.append(x)
        i += 1
        continue

'''
def f(n):
    # gets the nth fibonacci number
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)
'''
print(q25())
# f(n) above works 100%, but I have a feeling it is 
# too slow to do recursively to get my 1000 digit number
