#My attempt
def reverse_words(text):
    list = text.split()
    res = []
    for i in list:
        res.append(i[::-1])
    return ' '.join(res)

#Other solutions

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

def reverse_words(str):
  #go for it
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)