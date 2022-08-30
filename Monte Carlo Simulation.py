''' NAME: Akanksha Kakar
COURSE: CMPSC 131
INSTRUCTOR: Seth Volpe 
PROJECT NAME: Introduction to Programming Techniques: Monte Carlo Simulation (Project 2)
DATE OF COMPLETION: October 19, 2019
DATE OF SUBMISSION: October 21, 2019 '''
'''PROJECT DESCRIPTION (Objective): To create a program that
1. Generates a random number from 3 to 20, including 3 and 20
2. Uses that value to determine the Fibonacci number in the series
3. Uses the Fibonacci number as your radius for the circle
BONUS
Use the last trial and create a graphic representation of the simulation.
1.Draw a square and corresponding circle (you do not need the grid)
2.Draw each (x,y) point on the square/circle'''

#importing classes random and math
import random
import math

#method to get the fibonacci number at the nth position
def getFibonacci(n):
    #if n is 0, returning 0, or if n is 1, returning 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    #otherwise returning the sum of two previous fibonacci numbers
    return getFibonacci(n-1) + getFibonacci(n-2)

#method to run the simulation
def simulation():
    #total number of points to be generated per trial
    points = 1000000
    #number of trials
    trials = 10
    #finding a random fibonacci number as the radius and using this same radius throughout the trials(as mentioned)
    radius = getFibonacci(random.randint(3,20))
    #sum of probabilities of all trials
    sum_percentages = 0
    
    #loop to display each trial
    for i in range(1,trials+1):
        #displaying trial number
        print('Trial {}:'.format(i))
        #displaying radius
        print('Radius of the circle is {}'.format(radius))
        #finding the actual probability (circle area/ square area)*100
        probability = (math.pi*radius*radius / (2*radius)**2)*100
        #number of hits
        hits = 0
        
        #looping for points number of times
        for j in range(points):            
            #generating two random coordinates between (-radius, radius)
            x = random.uniform(-radius,radius)
            y = random.uniform(-radius,radius)
            #finding distance from center using distance formula, here center is origin
            dist_from_center = math.sqrt(x*x+y*y)
            #if distance is less than or equal to radius, its a hit
            if dist_from_center <= radius:
                hits += 1
        #finding simulated probability
        simulated_probability = float(hits)/float(points)*100
        #adding to sum_percentages
        sum_percentages += simulated_probability
        #displaying stats for this trial
        print("The probability of a point falling in the circle is {:.2f}%".format(probability))
        print("Simulation resulted in {:d} hits inside the circle or {:.2f}%".format(hits, simulated_probability))
        
    #finding average percentage
    avg_percentage = float(sum_percentages/trials)
    
    #displaying average percentage
    print("Average probability of all trials is {:.2f}%".format(avg_percentage))

#running simulation()
simulation()

 #end of program
