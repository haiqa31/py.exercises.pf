#Exercise no:1
num=int(input("enter a number: ")) 
#check if the number is even or odd 
if num%2==0:
     print("the number is even")
else:
     print("the number is odd")

#Exercise no:2
year=int(input("enter a year"))
if(year%400==0) or (year%4==0) and year%100!=0: 
 print(f"it is a leap year")
else:
    print(f"it is not a leap year")

#Exercise no:3 
age=int(input("enter your age")) 
if age>=18: 
    print("you are an adult") 
else:
  print("you are a minor")

#Exercise no:4
   #simple login system 
username="haiqa khan" 
password="12345"
user_name=input("enter your username:")
user_password=input("enter your password:") 
if username == user_name and password == user_password:
     print("login sucessfully") 
else:
    print("username and password is invalid")

#Exercise no:5
num=int(input("enter a number:"))
if num>0: print("positive")
elif num<0:
     print("Negative") 
else:
    print("zero")