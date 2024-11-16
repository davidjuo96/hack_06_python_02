def fn_hack_7(s):
    result = s
    i = 0
    
    if result == [0]:
        return [0]
    
    while len(result) > i:
        if i%2 != 0:
            result.pop(i)
            result.insert(i,i+1)
            
        else:
            result.pop(i)
            result.insert(i,str(i+1))
        
        i = i + 1
        
    return result