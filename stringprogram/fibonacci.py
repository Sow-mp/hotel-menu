n=int(input("enter the number"))
a=0
b=1
print(a,b,end=" ")
for _ in range(n):
    next_term=a+b
    print(next_term,end=" ")
    a,b=b,next_term
print()
