def fn_hack_9(s):
    result = {}
    
    if "foo" in s:
        value = s["foo"].replace("k","")
        result["Foo"] = value.capitalize()
        
    return result