# Question 16(b)
# Examination Number:

# For this question it is useful to understand ...
# 1. randint(a, b) returns a random integer N such that a<=N<=b.
# 2. s.append(x) appends the element x to the end of list s.

from random import *

heights = [] # an empty list of heights
weights = [] # an empty list of weights
bmi_values = [] # an empty list of bmi values

pairs = int(input('Enter the number of pairs of values you wish to generate: ')) # (ii)

# Loop to build up the lists with random values
for count in range(pairs): # (ii)
    # a random integer between 150 and 210
    heights.append(randint(150, 210))
    # a random integer between 50 and 130
    weights.append(randint(50, 130))
    # (iii) can be used here also without need for seperate loop
    #bmi_values.append(round(weights[count]/pow(heights[count],2)*10000,1))
    
    
# (iii)
for i in range(pairs):
    bmi_values.append(round(weights[i]/pow(heights[i],2)*10000,1))


# Display the lists
print(f'Heights: {heights}') # (i)
print(f'Weights: {weights}') # (i)
print(f'BMI values: {bmi_values}') # (iii)