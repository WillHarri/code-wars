def validate_pin(pin):
    if len(pin) == 6 and pin.isnumeric():
        return True
    elif len(pin) == 4 and pin.isnumeric():
        return True
    else:
        return False
    
#Other solution
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()