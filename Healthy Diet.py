#EXAM 1: FALL 2019
''' NAME: Akanksha Kakar
COURSE: CMPSC 131
INSTRUCTOR: Seth Volpe 
EXAM NO.: Exam 1
SESSION: Fall 2019
PROGRAM DESCRIPTION: Program to use the user's age to determine several pieces of information.
The following must be calculated:
1. Number of days, minutes and seconds that you have been alive (just multiple by 365)
2. Estimates the approximate number of times the user's heart has beat in his/her lifetime using an average heart rate of 72 beats per minute.
3. Ask the user to pick a item to eat for each meal. Based on their selections we will calculate how many calories they consumed in a day.
(if the result is larger than 2000, output that they are not eating a healthy diet.  Otherwise, they are eating healthy)
'''

# 1. Taking input for the age of the user
age = int(input("Enter your age(in years): "))

# Converting the age entered by the user into days, minutes and seconds
# Converting the age entered by user in DAYS
ageInDays = age * 365
print("User's age in days is ", ageInDays, " days")

# 2. Converting the age entered by user into MINUTES
ageInMinutes = ageInDays * 24 * 60

# 3. Printing the age in MINUTES
print("User's age in minutes is ", ageInMinutes, " minutes")

# 4. Converting the age entered by user into SECONDS
ageInSeconds = ageInMinutes * 60

# 5. Printing the age in SECONDS
print("User's age in seconds is ", ageInSeconds, " seconds")

# Calculating the approximate number of heartbeats in the user's lifetime
heartbeats = ageInMinutes * 72
print("Number of heartbeats in the user's life:", heartbeats)

# Calculating the total daily calorie count
totalDailyCalorieCount = 0
print("Please select an item for breakfast, lunch and dinner.")
print("Breakfast options:")
print("1. Omelete (250 calories)\n2. Bagel (280 calories)\n3. Sausage gravy over biscuits (590 calories)\n4. Pancakes (620 calories)")
# 6. Inputing the user's breakfast selection and store in a variable called breakfast
breakfast = int(input("Enter your breakfast selection: "))
# 7. Complete the set of if statements and update the total daily calorie count
if breakfast == 1:
    totalDailyCalorieCount = 250
elif breakfast == 2:
    totalDailyCalorieCount = 280
elif breakfast == 3:
    totalDailyCalorieCount = 590
elif breakfast == 4:
    totalDailyCalorieCount = 620

print("Lunch options:")
print("1. Salad (450 calories)\n2.Italian Hoagie (680 calories)\n3. Cheeseburger (620 calories)\n4. BLT (500 calories)")
# Inputing the user's lunch selection and store in a variable called lunch
lunch = int(input("Select the lunch option: "))
# 8. Completing the set of if statements and update the total daily calorie count
if lunch == 1:
    totalDailyCalorieCount += 450
elif lunch == 2:
    totalDailyCalorieCount += 680
elif lunch == 3:
    totalDailyCalorieCount += 620
elif lunch == 4:
    totalDailyCalorieCount += 500
print("1. Steak and vegtables (850 calories)\n2. Salmon and rice (380 calories)\n3. Chicken Parmesan with Pasta (1300 calories)\n4. Steak Salad (420 calories)")
# Inputing the user's dinner selection and store in a variable called dinner
dinner = int(input("Select the dinner option: "))
# 9. Completing the set of if statements and update the total daily calorie count
if dinner == 1:
    totalDailyCalorieCount += 850
elif dinner == 2:
    totalDailyCalorieCount += 380
elif dinner == 3:
    totalDailyCalorieCount += 1300
elif dinner == 4:
    totalDailyCalorieCount += 420

print("The total Calorie Count for today is: ", totalDailyCalorieCount)
if totalDailyCalorieCount > 2000:
    print("That is not a healthy diet!")
else:
    print("That is a healthy diet.")
#End of program
