y=int(input("enter the year:"))
if(y%4==0 and y%100!=0)or(y%400==0):
    print('leap year')
else:
    print("not leap year")


