def remove_smallest(numbers):
    new_list = []
    count = 0
    for i in numbers:
        if i == min(numbers) and count == 0:
            count += 1
        elif count > 0:
            new_list.append(i)
        elif i != min(numbers):
            new_list.append(i)
    return new_list

#Other solution
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a