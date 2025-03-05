def century(year):
    if year % 100 == 0:
        return year/100
    else:
        return int(year/100) + 1
    
#Other solution
def century(year):
return (year + 99) // 100