
a=int(input("enter the  number"))

def checkprime(a):
    if a>1:
        for j in range(2,int(a/2)+1):
            if(a%j)==0:
                print(a,"not prime num")
                break
            else:
                print("prime no")
    else:
        print("no prime num")
checkprime(a)



