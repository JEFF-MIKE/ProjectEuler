lst = [1,2,5,10,20,50,100,200] #list of possible coins
maxi = 200
mem = {}
def dp(arr,total,i,mem):
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        ret = dp(arr,total,i-1,mem)
    else:
        ret = (dp(arr,total-arr[i],i-1,mem) + dp(arr,total,i-1,mem))
    mem[key] = ret
    print(mem)
    return ret
    
def count_sets_dp(arr,total):
    #stores the amount of sets which adds up to 200
    mem = {}
    return dp(arr,total,len(arr)-1,mem)
    
#print(count_sets_dp(lst,maxi))

def count_sets(arr,total):
    #recursive solution to counting to 200
    