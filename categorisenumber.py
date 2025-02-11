#My solution

def open_or_senior(data):
    results = []
    for i in data:    
        if i[0] > 54 and i[1] > 7:
            results.append("Senior")
        else:
            results.append("Open")
    return results

#Other solution
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]