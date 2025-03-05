def digitize(n):
    res = [int(i) for i in str(n)]
    res.reverse()
    return res

#other solution

def digitize(n):
    return [int(x) for x in str(n)[::-1]]
