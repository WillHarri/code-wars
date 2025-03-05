def find_it(seq):
    for i in seq:
        tally = seq.count(i)
        if tally % 2 == 1:
            odd_num = i
    return odd_num

#Other solutions
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i