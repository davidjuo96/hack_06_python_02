def fn_hack_6(s):
    result = s
    
    if not result:
        return ["0"]
    
    for i in range(len(result)):
        if i%2 != 0:
            result.pop(i)
            result.insert(i,"-")
        else:
            result.pop(i)
            result.insert(i,str(i+1))
    
    return result