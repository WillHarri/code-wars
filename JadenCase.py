#My initial attempt
def to_jaden_case(string):
    string = string.split()
    for word in string:
        word = word.capitalize()
    return string

#Working solutions
def to_jaden_case(string):
    return ' '.join([word.capitalize() for word in string.split()])

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
