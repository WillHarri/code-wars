def get_middle(s):
    
    if len(s) % 2 == 0:
        return s[len(s)//2 - 1] + s[len(s)//2]
    else:
        return s[len(s)//2]
    

#Another solution
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]