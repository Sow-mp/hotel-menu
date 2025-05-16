def print_substr(str):
    n=len(str)
    for i in range(n):
        for j in range(i+1,n+1):
            print(str[i:j])
str="abc"
print_substr(str)

def sub_str(str):
    n=len(str)
    for i in range(n):
        for j in range(i+1,n+1):
            print(str[i:j])
str="ab"
sub_str(str)

''' i=0,j=1to 3 0:1 a
j=2 0:2 ab
j=3 0:3 012 abc
i=1 j=2to 3  1:2 b
j=3 1:3 1 2 bc
i=2  2+1=3to 4
2:3 c
2:4 
'''