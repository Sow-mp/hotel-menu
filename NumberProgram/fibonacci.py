num=int(input("Enter the number"))
a,b=0,1
if num<=0:
    print("positive num only ")
elif num==1:
    print("fibonacci series:0")
else:
    print("fibonacci sequense are:")
    for _ in range(1,num+1):
        print(a,end=" ")
        a,b=b,a+b

num=input("enter the number")
a,b=0,1
if num<0:
    print("positive num")
elif num==1:
    print(" fibonacci series:0")
else:
    print("fibonacci series: ")
    for _ in range(1,num+1):
        print(a,end=" ")
        a,b=b,a+b
