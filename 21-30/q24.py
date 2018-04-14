from itertools import permutations
def q24():
    # very specific question: I presume it is to try
    # and show off itertools
    x = list(permutations([0,1,2,3,4,5,6,7,8,9]))
    x.sort()
    return x[999999]
print(q24())