#Exercise 6: #Find and print the maximum of three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: ")) 
num3 = float(input("Enter the third number: "))
max_number = max(num1, num2, num3)
print("The maximum number is:", max_number)

  #Exercise no:7
   #GRADING SYSTEM
score = int(input("Enter the student's score: "))
if score >= 90: 
    print("your grade is A")
elif score >= 80: 
    print("your grade is B")
elif score >= 70:
    print("your grade is C")
elif score >= 60: 
    print("your grade is D") 
else: print("your grade is F")

#Exercise no:8
num= int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
         if num % i == 0: 
            print("Not a prime number")
            break 
         else: print("Prime number")
else: print("Not a prime number")

 #Exercise no:9
num= int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
         if num % i == 0: 
            print("Not a prime number") 
            break
    else:
             print("Prime number")
else: 
    print("Not a prime number")

#Exercise no:10
num1=int(input("enter the first number: ")) 
num2=int(input("enter the first number: ")) 
if num1 > num2:
     print(f"The larger number is: {num1}") 
elif num2 > num1:
     print(f"The larger number is: {num2}")