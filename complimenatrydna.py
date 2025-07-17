def DNA_strand(dna):
    res = []
    for i in dna:
        if i == 'A':
            res.append('T')
        elif i == 'T':
            res.append('A')
        elif i == 'C':
            res.append('G')
        elif i == 'G':
            res.append('C')
    return ''.join(res)

#Other Solution
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])