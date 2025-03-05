
def disemvowel(string_):
    for i in string_:
        vowels = 'AEIOUaeiou'
        res = ''.join([(i) for i in string_ if i not in vowels])
    return res

#Remember to use join instead of replace for iterations