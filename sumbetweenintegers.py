#My attempt

def get_sum(a,b):
    if a == b:
        return a
    else:
        return   sum(range(a+1,b)) + a + b
    
#Working solution
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))