def consonant_count(sentence):
    consonants = 0
    for i in sentence:
        if i.lower() not in 'AEIOUaeiou ':
            consonants += 1
    print (consonants)

consonant_count('All cows eat grass')