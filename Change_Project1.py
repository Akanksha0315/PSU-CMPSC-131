''' NAME: Akanksha Kakar COURSE: CMPSC 131 INSTRUCTOR: Seth Volpe
PROJECT NAME: Introduction to Programming Techniques: Making Changes
(Project 1) DATE OF COMPLETION: September 15, 2019 DATE OF SUBMISSION:
September 18, 2019 PROJECT DESCRIPTION (Objective): To create a program
that “makes change” for the user. The user will input two numbers, one
is the amount charged and the other is the amount given. The program
will determine the amount of change returned based on our currency. It
should return the bills (if any) and the coins. '''
#Taking input from user for the amount charged (float type)
charged = float(input("Enter the amount due: $ "))

#Taking input from user for the amount paid by the user (float type)
paid = float(input("Enter the amount paid: $ "))

#displaying the information entered by user
print("Amount Due: $ ", charged)
print("Amount Paid: $ ", paid)
 
#calculating the amount of change to be returned to the user
change = paid - charged
change = round(change,2)
 
#checking conditions to determine if any change is to be returned or not
if change < 0:
    print("Amount paid is not sufficient")
    #calculating amount that was left to be paid
    pay = ((-1)*change)
    pay = round(pay,2)
    #displaying required message
    print("Amount left to be paid: $ ", pay)
elif change == 0:
    #displaying required message
    print("Amount paid. No change to be returned ")
else:
    #displaying required message
    print("Change Due : $ ", change)
    #breaking down the change to be returned to the user
    #considering that change does not exceed 20 dollar bills 
    change = (change * 100)
    
    if change//2000 != 0:
        if change//2000 == 1:
            print(int(change//2000), " twenty dollar bill")
        else:
            print(int(change//2000), " twenty dollar bills")
        change = (change % 2000)
        
    if change//1000 != 0:
        if change//1000 == 1:
            print(int(change//1000), " ten dollar bill")
        else:
            print(int(change//1000), " ten dollar bills")
        change = (change % 1000)
    	
    if change//500 != 0:
        if change//500 == 1:
            print(int(change//500), " five dollar bill")
        else:
            print(int(change//500), " five dollar bills")
        change = (change % 500)
	
    if change//100 != 0:
        if change//100 == 1:
            print(int(change//100), " one dollar bill")
        else:
            print(int(change//100), " one dollar bills")
        change = (change % 100)
	
    if change//25 != 0:
        if change//25 == 1:
            print(int(change//25), " quarter")
        else:
            print(int(change//25), " quarters")
        change = (change % 25)
        
    if change//10 != 0:
        if change//10 == 1:
            print(int(change//10), " dime")
        else:
            print(int(change//10), " dimes")
        change = (change % 10)
	
    if change//5 != 0:
        if change//5 == 1:
            print(int(change//5), " nickel")
        else:
            print(int(change//5), " nickels")
        change = (change % 5)
	
    if change//1 != 0:
        if change//1 == 1:
            print(int(change//1), " penny")
        else:
            print(int(change//1), " pennies")

#displaying the required details of the amount of change due
