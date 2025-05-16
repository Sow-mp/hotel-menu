def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
word1 = input("enter the string1")
word2 =input("enter the string2 ")

if are_anagrams(word1, word2):
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are NOT anagrams.')

word1=input("enter the string")
word2=input("enter the string")

def anagram(word1,word2):
    return sorted(word1)==sorted(word2)

if anagram(word1,word2):
    print(f"anagram")
else:
    print(f"not anagram")
