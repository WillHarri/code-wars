def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

#Other solution
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])