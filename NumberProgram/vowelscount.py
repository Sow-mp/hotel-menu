
num=input("enter the string: ")
vow="aeiouAEIOU"
count=sum(1 for char in num if char in vow)
print("sum of count:",count)

num=input("enter the str")
vow="aeiou"
count=sum(1 for char in num if char in vow)
print("sum of count:",count)
