# lab1_calculatePi.py

# Brianna Drew
# January 19, 2021
# ID: #0622446
# Lab #1, Part #3

# import required modules
import random
import math
import time

inside = 0 # counter for points that are inside the circle
outside = 0 # counter for points that are outside the circle
iterations = 1000000 # number of points to generate

# seed the random number generator
random.seed(int(round(time.time()*1000)))

for i in range(iterations):

    # generate two random numbers from 0 to 1
    x = random.random()
    y = random.random()
    
    # calculate distance from origin
    dist = math.sqrt((x*x) + (y*y))
   
   # determine whether the point is inside or outside the circle
    if dist < 1 :
        # increment counter for inside
        inside += 1
    else:
        # increment counter for outside 
        outside += 1
     
# print how many points fall inside the circle and how many fall outside     
print("inside: ", inside, ", outside: ", outside)

# calculate the estimated value of pi 
pi = (inside / iterations) * 4

# print result
print("Pi Estimation: ", pi)