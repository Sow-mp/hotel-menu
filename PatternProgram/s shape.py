n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or i==n//2):
            print("*",end=" ")
        elif(i<n//2 and j==0):
            print("*",end=" ")

        elif(i>n//2 and j==n-1):
            print("*", end=" ")
        else:
            print(" ",end=" ")

    print()
print()
print()

n = 5
for i in range(n):  # Outer loop for rows (0 to 4)
    for j in range(n):  # Inner loop for columns (0 to 4)
        if (i == 0 or i == n // 2 or i == n - 1):
            print("*", end=" ")
        elif (i < n // 2 and j == 0):
            print("*", end=" ")
        elif (i > n // 2 and j == n - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next line after printing each row
