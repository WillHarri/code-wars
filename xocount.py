#My first attempt
def xo(s):
    x_count = 0
    o_count = 0
    for i in str(s):
        if i == 'x' or 'X':
            x_count +=1
        elif i == 'o' or 'O':
            o_count +=1
    if x_count == o_count:
        return True
    else:
        return False
    
#Second attempt (passed)
def xo(s):
    x_count = s.count('x') + s.count('X')
    o_count = s.count('o') + s.count('O')
    if x_count == o_count:
        return True
    else:
        return False

#Best solution
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')