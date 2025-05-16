n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()


n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()