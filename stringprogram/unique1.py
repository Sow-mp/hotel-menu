res=input("Enter the string:")
f=0
for i in range(len(res)):
    for j in range(i+1,len(res)):
        if res[i]==res[j]:
            f=1
        break
if f==0:
    print(" unique")
else:
    print("not uniqu")


res=input("enter the str")
f=0
for i in range(len(res)):
    for j in range(i+1,len(res)):
        if res[i]==res[j]:
            f=1
            break

if f==0:
    print("u")
else:
    print("not u")

