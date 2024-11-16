def fn_hack_3(s):
    result = s
    vowels = "aeiou"
   
    if result[0].lower() not in vowels:
        result = result[0].upper() + result[1:]
    
    if result[-1].lower() not in vowels:
        result = result[:-1] + result[-1].upper()
        
    result = result.replace("a", "@").replace("e", "3").replace("i", "¡").replace("o", "0").replace("u", "v")
    
    return result