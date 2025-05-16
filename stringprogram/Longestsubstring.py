# input=s="aaabb",k=3
#output=3 ,divide and conquer,sliding window

def Longest_substring(s,k):

    if len(s)<k:
        return 0
    char_count={ }
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1

    for char in char_count:
        if char_count[char]<k:
            max_length=0
            for part in s.split(char):
                max_length=max(max_length,Longest_substring(part,k))
            return max_length
    return len(s)

print(Longest_substring("aaabbc",1))

