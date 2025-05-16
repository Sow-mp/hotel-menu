res=input("Enter the string:")
f=0
for i in range(len(res)):
    for j in range(i+1,len(res)):
        if (res[i]==res[j]):
            f=1
            break
if f==0:
  print("string is unique")
else:
    print("string is not unique")

res = input("Enter the string: ")
if len(res) == len(set(res)):  # Convert to set and compare lengths
    print("String is unique")
else:
    print("String is not unique")


