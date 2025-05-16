def compressed_str(s):
    compressed_res=[]
    count=1
    for i in range(1,len(s)):#aaa
        if s[i]==s[i-1]:
            count+=1
        else:
         compressed_res.append(s[i-1]+str(count))
         count=1#aaabbcc
    compressed_res.append(s[-1]+str(count))#c2
    compressed_str=''.join(compressed_res)#a3

    if len(compressed_str)<len(s):
        return compressed_str
    else:

        return s

print(compressed_str("pppppprrrr"))

def compressed_res(s):
    compressed_str=[]
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
           compressed_str.append(s[i-1]+str(count))
           count=1
    compressed_str.append(s[-1]+str(count))






def compressed_str(s):
    if not s:
        return s

    compressed_res = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_res.append(s[i - 1] + str(count))
            count = 1

    # Append the last character group
    compressed_res.append(s[-1] + str(count))

    compressed_string = ''.join(compressed_res)

    # Return compressed string only if it's shorter
    if len(compressed_string) < len(s):
        return compressed_string
    else:
        return s

print(compressed_str("aaabbcc"))  # Output: a3b2c2
