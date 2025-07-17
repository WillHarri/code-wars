def unique_in_order(sequence):
    res=[]
    previous = ''
    for i in sequence:
        if i != previous:
            res.append(i)
            previous = i
    return res

unique_in_order("AAAABBBCCDAABBB")