n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(p,end=" ")
    p=p+1
    print()


n = 5
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Print the same number i, i times
    for j in range(2 * i - 1):
        print(i, end=" ")

    print()  # Move to next line



