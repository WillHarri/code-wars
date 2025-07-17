def accum(st):
    res = []
    index=0
    for i in st:
        if i == st[0] and i not in res:
            res.append(i.upper())
        else:
            res.append(i.upper() + (i.lower()*index))
        index+=1
    return '-'.join(res)

#Other Solution
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))