# it works, and is fast, but the code is something you'd see
# from shitcode.com

def q52():
    # find the smallest positive
    # x, such that 2x,3x,4x,5x and 6x
    # all contain the same digits
    i = 1
    # declare here so python doesn't copy over and over
    while True:
        # do a long ass check first
        if len(str(i*2)) == len(str(i*3)):
            if len(str(i*3)) == len(str(i*4)):
                if len(str(i*4)) == len(str(i*5)):
                    if len(str(i*5)) == len(str(i*6)):
                        # okay, they are the same length, NOW 
                        # you can actually check their numbers
                        int2 = str(i*2)
                        int3 = str(i*3)
                        int4 = str(i*4)
                        int5 = str(i*5)
                        int6 = str(i*6)
                        d = {int2:{},int3:{},int4:{},int5:{},int6:{}}
                        # generate dictionaries with their numbers in them
                        keyArray = []
                        for key in d:
                            for letter in key:
                                if letter not in d[key]:
                                    d[key][letter] = 1
                                else:
                                    d[key][letter] += 1
                            keyArray.append(d[key])
                        # now check to see if they are all equal or not
                        # verbose, but is neater than the possible one liner
                        flag1 = keyArray[0] == keyArray[1]
                        flag2 = keyArray[1] == keyArray[2]
                        flag3 = keyArray[2] == keyArray[3]
                        flag4 = keyArray[3] == keyArray[4]
                        if flag1 == True and flag2 == True and flag3 == True and flag4==True:
                            print(i)
                            print(keyArray)
                            return
        i+=1               

q52()      

        
