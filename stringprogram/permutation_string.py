# without useing the string functions
def find_permutation(s):
    if len(s)==1:
        return [s]
    permutation=[]
    for i in range(len(s)):
            current_char=s[i]
            remaining_char=s[:i]+s[i+1:]
            remaining_permutations=find_permutation(remaining_char)

            for p in remaining_permutations:
                permutation.append(current_char+p)
    return permutation

print(find_permutation("abc"))