def square_digits(num):
    number = []
    for i in str(num):
        i = int(i)**2
        number.append(i)
        for i in number:
            res=''.join([str(i) for i in number])
    return int(res)

#Other solution
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)