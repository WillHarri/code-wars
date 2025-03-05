def find_short(s):
    s = s.split()
    l = min(len(i) for i in s)
    return l

def find_short(s):
    return min(len(x) for x in s.split())