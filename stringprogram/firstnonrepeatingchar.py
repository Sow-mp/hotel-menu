def first_non_reapeating_char(s):
    char_count={}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1

    for i in range(len(s)):
        if char_count[s[i]]==1:
            return i

    return -1

print(first_non_reapeating_char("swiss"))