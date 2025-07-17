def rental_car_cost(d):
    initial_cost = d * 40
    if d >= 7:
        return initial_cost - 50
    elif d >= 3:
        return initial_cost - 20
    else:
        return initial_cost
    

    def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result