n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

n = 5
for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    print()


n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")

    print()

n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")

    print()


n=5
for i in range(n):
    for j in range(n):
       if i==n//2 or j==n//2:
           print("*",end=" ")
       else:
           print(" ",end=" ")
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

n=5
for i in range(1,n+1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n+1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
print()

n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1:
            print("*",end=" ")
        else:
            print("  ",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()




