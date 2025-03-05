def hammingdistance(string1, string2):
    differences = 0
    index = range( len(string1))
    for i in index:
        if string1[i] != string2[i]:
            differences += 1
    print(differences)

hammingdistance('what', 'fhat')