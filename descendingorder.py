#My solution attempt

def descending_order(num):
    num = list(map(int,str(num)))
    num = num.sort(Reverse = True)
    result = int("".join(map(str, num)))
    return result

#Correct solution

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))