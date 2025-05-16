def roman_to_integer(s):
    roman_values={
        'I':1,'V':5,"X":10,
        "L":50,"C":100,"D":500,"M":1000

    }
    total=0
    prev_value=0
    for char in reversed(s):
        curr_value=roman_values[char]

        if curr_value<prev_value:
            total-=curr_value
        else:
            total += curr_value

        prev_value=curr_value
    return total

print(roman_to_integer("MMXCIV"))

def roman_to_integer(s):
    roman_values={"I":1,"V":5,"X":10,'L':50,
                  "C":100,'D':500,"M":1000}

    t=0
    pv=0
    for char in reversed(s):
        cv=roman_values[char]

        if cv<pv:
            t-=cv
        else:
            t+=cv

        pv=cv
    return t














