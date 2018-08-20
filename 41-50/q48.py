def q48():
    # ez mode
    # pfffttttt
    total = 0 
    for i in range(1,1001):
        total += (i ** i)
    total = str(total)
    answer = total[-10::]
    print(answer)
q48()