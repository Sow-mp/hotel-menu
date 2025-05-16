num=int(input("enter the num:"))
order=len(str(num))
sum_num=sum(int(digit)**order for digit in str(num))
if num==sum_num:
    print("Armstrong")
else:
    print("Not Armstrong")

num=input("Enter the number")
order=len(str(num))
sum=sum(int(digit)**order for digit in str(num))
if num == sum:
    print("a")
else:
    print("not a")


