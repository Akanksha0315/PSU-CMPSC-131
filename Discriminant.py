'''PROGRAM DESCRIPTION: Program to taking input from users for the values of
A,B and C and to calculatethe discriminant using these 3 values (where A cannot
equal zero)'''
# Discriminant (D) = B^2 - (4*A*C)
# 1. Input the data for variables A, B and C
A = float(input("Enter the value for variable A: "))
B = float(input("Enter the value for variable B: "))
C = float(input("Enter the value for variable C: "))

# 2. Checking if A is equal to zero
#If A = 0, then taking a new input from user along with displaying an appropriate message
if A == 0:
    print("Your coefficient for 'A' MUST BE a value greater than 0, otherwise your equation is not a quadratic!")
    A = float(input("Please enter a new value for A: "))

#Importing the math library
import math

#Computing the discriminant
# 3. Calculating the discriminant vaue and storing it in variable disc
disc = (B*B) - (4*A*C)

#Display the disciminant computed.
print("\nThe discriminant of the equation is", str(disc) + ".")

#Checking the sign of the computed discriminant
#This tells us if the number is real or imaginary solutions.
#If there are real solutions, use the quadratic formula to solve for x.
#Display the number of solutions and values for x, (if computed).

# 4. Checking if the value of disc equals 0
if disc == 0:
    print("This equation has 1 real solution.")
    x = ((-B + math.sqrt(disc)) / (2 * A))
    print("The solution to your equation is: ", x)

# 5. Check to see if disc is greater than 0
if disc > 0:
    print("This equation has 2 real solutions.")
    x1 = ((-B + math.sqrt(disc)) / (2 * A))
    x2 = (-B - math.sqrt(disc)) / (2 * A)
    print("One solution to the equation is: ", x1)
    print("The other solution to the equation is:", x2)

# 6. Check to see if disc is less than 0
if disc < 0:
    print("This equation has 2 imaginary solutions.")
