import calendar

y=int(input("enter the year"))
m=int(input("enter the month"))

res=calendar.month(y,m)
print(res)

def numbercheck(a):
    if a>0:
        print("pos")
    elif a<0:
        print("neg")
    else:
        print("zero")


a=int(input("enter the number"))
numbercheck(a)