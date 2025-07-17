#Solution
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old)


def twice_as_old(dad_years_old, son_years_old):
    age = dad_years_old
    original_son_years_old = son_years_old
    original_dad_years_old = dad_years_old
    while dad_years_old != son_years_old * 2:
            while son_years_old > 0:
                dad_years_old -= 1
                son_years_old -= 1
            original_dad_years_old += 1
            original_son_years_old += 1
            dad_years_old = original_dad_years_old
            son_years_old = original_son_years_old
    return abs(dad_years_old - age)

print (twice_as_old(36,7))