#importing random class
import random

#initializing variables
green = 0
yellow = 0
red = 0

#Running a loop until green, yellow and red is 10(Using for loop)
for loop in range(1,20,1):
    if green < 10 and yellow < 10 and red < 10:
        speed = int(input("Enter a speed observed: "))
        if speed >= 50:
            print("Speed classification was Green")
            green += 1
        elif speed >= 25:
            print("Speed classification was Yellow")
            yellow += 1
        else:
            print("Speed classification was Red")
            red += 1

# Displaying the Traffic Count Summary based off values inputed by user
print("/n TRAFFIC COUNT SUMMARY ")
print("Green Speed Classification Count: ", green)
print("Yellow Speed Classification Count: ", yellow)
print("Red Speed Classification Count: ", red)
#End of program

         
