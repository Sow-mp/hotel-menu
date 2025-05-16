def to_upper_string(s):
    res=" "
    for char in s:
        if "a"<=char<="z":
            res+=chr(ord(char)-32)#ord gives the ascii value
        else:#chr convert ascii  to char
            res+=char
    return res


print(to_upper_string("python"))

def to_upper(s):
    res=" "
    for char in s:
        if "A"<=char<="Z":
            res+=chr(ord(char)+32)
        else:
            res+=char
    return res

print(to_upper("Pprr"))