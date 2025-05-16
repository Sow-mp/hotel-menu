n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()


n=5
p=1
for i in range(1,n+1):
    for j in range(i):
        print(p,end=" ")
    p=p+1
    print()#7829970243#18002583838

n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
