from math import factorial
def q34():
    # Much simpler than what I initially thought.
    # just record the factorial for each number in a dictionary
    # then just access it over the loop per number
    answer_list = []
    d = dict()
    for i in range(10):
        d[i] = factorial(i)
    for x in range(10,100000):
        z = [int(y) for y in str(x)]
        for c in range(len(z)):
            z[c] = d[z[c]]
        u = sum(z)
        if u == x:
            answer_list.append(u)
    print(answer_list)
    print(sum(answer_list))
# I got lucky with this one and it just so happened only 2 numbers
# were involved in my answer below 100,000 (145,40585)
q34()