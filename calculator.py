while True:
   num1=eval(input("enter the first value:"))
   num2=eval(input("enter the second value:"))
   opr=input("enter the opr..(+,-,/,%,*)")

   if opr=='+':
    print(num1+num2)
   elif opr=='-':
    print(num1-num2)    

   elif opr=='/':
    print(num1/num2)

   elif opr=='*':
    print(num1*num2)

   elif opr=='%':
    print(num1%num2)
   else:
    print("invalid opr....")
    
