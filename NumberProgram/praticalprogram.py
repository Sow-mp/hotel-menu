str=input("enter the string:")
vow="aeiouAEIOU"
words=sum(1 for char in str if char in vow)

print(words)