def fn_hack_10(s):
    result = []
    x = 1
    y = 2

    for i in s:
        new_i = {}
        for _ in i:
            new_i[str(x)] = str(y)
            x = x + 2
            y = y + 2
        result.append(new_i)
        
    return result