def fn_hack_5(s):
    result = s
    vowels = "aeiou"
    
    if len(result) == 8:
        if (result[0] not in vowels and result[1] in vowels and result[2] in vowels):
            return f"{result[:2]}-{result[3:5]}-{result[5:7]}-"
        elif (result[0] not in vowels and result[1] in vowels and result[2] not in vowels):
            return f"{result[:2]}-{result[3:5]}-{result[6:]}"
    elif len(result) == 3 and (result[0] not in vowels and result[1] in vowels):
        return f"{result[:2]}-"
    else:
        return result