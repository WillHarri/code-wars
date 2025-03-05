def repeat_str(repeat, string):
    n=0
    list = []
    while n < repeat:
        list.append(string)
        n +=1
    string = ''.join(list)
    return string

def repeat_str(repeat, string):
    return repeat*string