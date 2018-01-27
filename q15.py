import math

def problem15(n):
    # determines the amount of possible paths in an (n*n) grid
    # This uses combinational mathemathics
    return math.factorial(n + n) / (math.factorial(n) * math.factorial(n)) 

#print(problem15(20)) this works 100%

def problem15i(n):
    # same as above, but using pascals triangle instead
    grid = []
    grid.append([1 for x in range(n)])
    for i in range(1,n):
        grid.append([0 for l in range(n)])
        grid[i][0] = 1
    # grid is setup, now is time for maths form
    across = 1
    down = 1
    while down != 20:
        grid[down][across] += (grid[down-1][across] + grid[down][across-1]) 
        across += 1
        if across == 20:
            down += 1
            across = 1
    return grid[-1][-1]
print(problem15i(20))


