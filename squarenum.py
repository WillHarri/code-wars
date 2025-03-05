import math
def is_square(n):
    if n < 0:
        return False
    else:
        return math.sqrt(n).is_integer()
    
    #Other solution
    import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;