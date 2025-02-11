#Combines an array of strings together to produce a sentence.
def smash(words):
    return "".join(str(x) + " " for x in words).strip()

#Better solution
def smash(words):
    return " ".join(words)