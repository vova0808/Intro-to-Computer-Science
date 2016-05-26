def bigger(a,b):
    if a > b:
        return a
    if a == b:
        return a
    else:
        return b
    

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    result = None
    if a > bigger(b, c):
        result = bigger(b, c)
    elif b > bigger(a, c):
        result = bigger(a, c)
    elif c > bigger(a, b):
        result = bigger(a, b)
        return result
        
        
