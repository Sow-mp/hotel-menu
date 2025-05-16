
def calculatelength(num):
     l=0
     while(num!=0):
         l=l+1
         num=num//10
     return l
n=175
r=0
s=0
l=calculatelength(n)
num=n

while num>0:
     r=num%10
     s=s+int(r ** l)
     num=num//10
     l=l-1

if(s==n):
    print("disarium")
else:
    print("not disarium")

