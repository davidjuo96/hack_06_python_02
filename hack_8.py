def fn_hack_8(s):
    result = []
    length = len(s)
    
    for i in range(length):
        if length % 2 != 0:
            result.append(f"{s[length - i - 1]}-{length - i}")
        else:
            result.append(str(length - i))
            
    return result