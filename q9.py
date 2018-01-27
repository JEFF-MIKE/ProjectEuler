import math

def problem9():
    a = 1
    b = 2
    while True:
        c = math.sqrt((a**2)+(b**2))
        if c.is_integer() == False or a + b + c != 1000:
            a += 1
            if a == b:
                a = 1
                b += 1
            continue
        if a + b + c == 1000:
            break
    print(a,b,c)
    return (a*b*c)

print(problem9())
        
