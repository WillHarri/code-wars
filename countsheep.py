def count_sheep(n):
    res = []
    for i in range(n+1):
        if i > 0:
            res.append(f'{i} sheep...')
    return ''.join(res)

#Other solutions
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep