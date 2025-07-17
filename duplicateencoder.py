def duplicate_encode(word):
    word = word.lower()
    res = []
    for i in word:
        count = word.count(i)
        if count == 1:
            res.append('(')
        else:
            res.append(')')
    return ''.join(res)

duplicate_encode('oIeQDvtu!(L@')