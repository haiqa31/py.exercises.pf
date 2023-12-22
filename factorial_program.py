num1=int(input("enter a number:"))
fact=1 
i=1 
if num1<0:
     print("Enter A GREATER NUMBER")
else:
     while i<=num1: 
        fact=fact*i
        i=i+1
        print("The factorial of",num1,"is",fact)