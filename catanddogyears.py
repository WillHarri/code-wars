def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = dog_years = 15
    elif human_years == 2:
        cat_years = dog_years = 9 + 15
    else:
        cat_years = 9 + 15 + ((human_years-2)*4) 
        dog_years = 9 + 15 + ((human_years-2)*5) 
    return [human_years,cat_years,dog_years]

#Other solution
def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    if human_years == 1:
        catYears += 15
        dogYears += 15
        return [human_years, catYears, dogYears]
    elif human_years == 2:
        catYears += 24
        dogYears += 24
        return [human_years, catYears, dogYears]
    elif human_years > 2:
        catYears += 24
        dogYears += 24
        years = human_years - 2
        catYears += years*4
        dogYears += years*5
        return [human_years, catYears, dogYears]
    return [0,0,0]