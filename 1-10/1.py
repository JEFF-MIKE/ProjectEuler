def problem1():
    # find the sum of all multiples of 3 or 5 below 1000
    answer = 0
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            answer += i
    return answer

#print(problem1())

def problem2():
    # find the sum of even-valued terms in the Fibonacci sequence
    # where the fibonacci sequence does not exceed 4 million
    answer = 0
    i = 2 # indexer
    fib = [0,1] # the fibonacci array sequence
    while fib[-1] < 4000000:
        k = fib[i-1] + fib[i-2]
        fib.append(k)
        i += 1
    for item in fib:
        if item % 2 == 0:
            answer += item # even numbers
    return answer

#print(problem2())
''' attempt1
def problem3(number):
    # The largest prime factor of the number "number"
    if number == 0:
        print("If statement is being executed!")
        return 0
    if number == 1:
        return "The number 1 is NOT a prime number!"
    largest = 0
    for i in range(2,number):
        for j in range(2,i):
            if i % j == 0: # is i a prime number? 
                break
        if number % i == 0 and i > largest:
            largest = i
            print(largest)
    return largest

print(problem3(600851475143))

'''
def problem3(number):
    # the largest prime factor of the number "number"
    a = number
    equation = ''
    b = 2
    c = 0
    primeFactor = {}
    while a != 1:
        if a % b == 0:
            a /= b
            if str(b) not in primeFactor:
                primeFactor[str(b)] = 1
            else:
                primeFactor[str(b)] += 1
            if b > c:
                c = b
            b = 2
        else:
            b += 1
    for key in primeFactor.keys():
        equation += "%s^%s\n" % (key,primeFactor[key])
    print(equation)
    return c
# every number n can have at most one prime factor greater than root n
# print(problem3(600851475143))

'''
def problem4():
    # find the largest palindrome made from the product of
    # two 3-digit numbers
    a = 100 # both 3 digit numbers
    b = 100
    largest = 0
    flag = True
    while b != 999:
        print(a)
        result = a * b
        # now we need to check for a palindrome
        result = str(result)
        ispalin = result.split(',')
        length = len(ispalin)
        for i in range(length):
            if ispalin[i] != ispalin[-1 *(i+1)]:
                flag = False
                break
        if not flag:
            largest = int(result)
        a += 1
        if a == 1000:
            a = 100
            b += 1
        if b == 1000:
            break
    return largest
'''
def problem4():
    status = False
    top = 999 * 999
    palindrome = []
    for number in range(top,10000,-1):
        number = str(number)
        string = [_ for _ in number]
        for i in range(len(string)):
            if string[i] != string[(-1*(i+1))]:
                break # exit this loop
            if (i+1) == len(string):
                status = True
        if status:
            status = False
            answer = ''.join(string)
            palindrome.append(answer)
    print(len(palindrome))
    print("STEP 1: DONE")
    # We have an array of the palindromes (only 5% of the numbers 
    # below 1,000,000 are palindromes) Now we check their product
    length = len(palindrome)
    for j in range(length):
        isthis = palindrome[-1*(j+1)]
        temp_lst = []
        a = 2
        counter = 0
        while isthis != 1:
            if isthis % a == 0:
                isthis //= a
                if a not in temp_lst:
                    temp_lst.append(a)
                a = 2
            else:
                a += 1
        for item in temp_lst:
            if len(str)
            item = str
            
        
        
