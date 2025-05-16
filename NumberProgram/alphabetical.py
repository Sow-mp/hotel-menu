
my_Str=input("Enter the string:")
#words=[word.capitalize() for word in my_Str.split()]
words=my_Str.split(" ")
words.sort()
#print(" sorted words are:")
for word in words:
     print(word)



import calendar
y=int(input(" enter the year"))
m=int(input(" enter the month"))

cal=calendar.month(y,m)
print(cal)


