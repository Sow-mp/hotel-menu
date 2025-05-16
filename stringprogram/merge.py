str=input("enter the string")
str1=input("enter the string")

def merge_str(str,str1):
    res=" "
    i=0
    while(i<len(str) or i<len(str1)):
        if i<len(str):
            res+=str[i]

        if i<len(str1):
            res+=str1[i]
        i=i+1
    return res


print(merge_str(str,str1))



s1=input("enter str")
s2=input("enter str")

def merge_str(s1,s2):
    i = 0
    res =" "
    while (i<len(s1) or i<len(s2)):
        if i<len(s1):
            res+=s1

        if i<len(s2):
            res+=s2

        return res

print(merge_str(s1,s2))

