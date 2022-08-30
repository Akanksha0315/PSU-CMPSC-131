#Input two numbers
numberOne = float (input("Enter a number: "))
numberTwo = float(input("Enter another number: "))
#calculate and display sum 
sum = numberOne + numberTwo
#Output 5 + 7 = 12
print (numberOne, " + ", numberTwo, " = ", sum)
#calculate and display difference
diff = numberOne - numberTwo
print (numberOne, " - ", numberTwo, " = ", diff)
#calculate and display product
prod = numberOne * numberTwo
#Output 5 * 7 = 35
print (numberOne, " * ", numberTwo, " = ", prod)
#calculate and display quotient
quot = numberOne / numberTwo
print (numberOne, " / ", numberTwo, " = ", quot)
#calculate and display modulus - cast to int
mod = int(numberOne) % int(numberTwo)
print (numberOne, " % ", numberTwo, " = ", mod)
#calculate and display sum of the results 
sum2 = sum + diff + prod + quot + mod
print ("Sum of results: " , sum2)
#calculate and display average of the two numbers
avg = (numberOne + numberTwo)/2
#Output (5 + 7)/2 = 6
print ("Average = ", avg)

