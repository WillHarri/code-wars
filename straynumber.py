def stray(arr):
    for i in arr:
        count = arr.count(i)
        if count == 1:
            res = i
    return res

#More efficient solution
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x