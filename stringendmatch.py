def solution(text, ending):
    text = text[-len(ending):]
    if ending == text:
        return True
    else:
        return False
    
#Better solution
def solution(string, ending):
    return string.endswith(ending)