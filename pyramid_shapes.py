#code for half pyramid shape of stars
n=int(input("enter the number for half pyramid : "))
for i in range (0,n):
     for j in range(1,i+1):
         print("*",end=" ")
         print("\n")

#code for inverted half pyramid shape of stars
n=int(input("enter the number for inverted half pyramid : "))
for i in range (n,0,-1):
     for j in range(1,i+1):
         print("*",end=" ")
         print("\n")

#code for hollow inverted half pyramid shape of stars
rows = int(input("Enter the number of rows for the hollow inverted half pyramid: ")) 
for i in range(rows, 0, -1):
     for j in range(1, i + 1):
         if j == 1 or j == i or i == rows:
             print("*", end=" ")
else: 
    print(" ", end=" ")
print()

  #code for full pyramid shape of stars
n=int(input("enter a number of rows for full pyramid shape : ")) 
for i in range(n):
     print(" " *(n - i - 1),end="")
     print(" *" * (i+1))

#code for inverted full pyramid shape of stars 
n=int(input("enter a number of rows for full pyramid shape : ")) 
for i in range(n, 0,-1): 
    print(" " *(n - i),end="")
print("* " * i)

#code for hourglass pyramid shape
size = int(input("Enter the size of the hourglass: "))
for i in range(size):
 spaces = ' ' * i
stars = '*' * (2 * (size - i) - 1)

print(spaces + stars)
for i in range(size - 2, -1, -1):
   spaces = ' ' * i
stars = '*' * (2 * (size - i) - 1)
print(spaces + stars)

#code for snowflake pyramid shape
size = int(input("Enter the size of the snowflake: "))
for i in range(size):
 print(' ' * (size - i - 1) + '*' * (2 * i + 1))
for i in range(size - 2, -1, -1):
 print(' ' * (size - i - 1) + '*' * (2 * i + 1))

#code for square shape pyramid
def square_constellation(size):
 for _ in range(size):
  print('* ' * size)
square_constellation(6)