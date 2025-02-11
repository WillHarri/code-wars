#My attempt
def fake_bin(x):
    for i in x:
        if int(i) < 5:
            i = 0
        else:
            i = 1
    return str(x)

#Correct solution
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

#Other solution
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result