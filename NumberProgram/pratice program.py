my_str=input("enter the string")
words=my_str.split()
words.sort()
for word in words:
    print(word)
import calendar
y=int(input("enter the year"))
m=int(input("enter the month"))
cal=calendar.month(y,m)
print(cal)
