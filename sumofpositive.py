def positive_sum(arr):
    positive = []
    for i in arr:
        if i > 0:
            positive.append(i)    
    return sum(positive)

#Other solutions
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum