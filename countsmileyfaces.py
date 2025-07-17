def count_smileys(arr):
    eyes = [';',':']
    noses = ['-','~']
    smiles = [')','D']
    faces = 0
    for i in arr:
        if i[0] in eyes and i[1] in smiles:
            faces +=1
        elif i[0] in eyes and i[1] in noses and i[2] in smiles:
            faces +=1
    return faces

#Other Solution
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count