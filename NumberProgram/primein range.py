
lower_range=int(input("enter the number1"))
upper_range=int(input("enter the number2"))

for num in range(lower_range,upper_range+1):
     if num>1:
         for i in range(2,num):
             if(num%i)==0:
                 break
         else:
             print(num)

 lr=int(input("enter the num1"))
 ur=int(input("enter the num2"))

 for num in range(lr,ur+1):
      if num>1:
          for i in range(2,num):
              if num%i==0:
                  break
          else:
              print(num)
