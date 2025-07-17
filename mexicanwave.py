def wave(people):
    people = list(people.lower())
    res = []
    count = 0
    for i in people:
        if i.isalnum():
            people[count] = i.upper()
            res.append(''.join(people))
            people[count] = i.lower()
        count += 1
    return res
    
wave(' Gap ')

#Other Solution
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]