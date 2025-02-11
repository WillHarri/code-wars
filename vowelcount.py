def get_count(sentence):
    count = 0
    vowels = 'aeiou'
    for i in sentence:
        if i in vowels: 
            count = count + 1
    return count

#Better solutions


def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


def getCount(s):
    return sum(c in 'aeiou' for c in s)