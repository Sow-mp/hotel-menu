str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Convert both strings to sets to find common characters
common_chars = set(str1) & set(str2)# intersect operation


# Remove spaces if needed
common_chars.discard(' ')


print("Common characters:", ''.join(common_chars))

s1=input("enter the strinh")
s2=input("enter")

comm=set(s1) & set(s2)
comm.discard(' ')
print("common: ",''.join(comm))