def square_sum(numbers):
    squared_num = []
    for i in numbers:
        i = i**2
        squared_num.append(i)
    return(sum(squared_num))
    
print(square_sum([1,2]))