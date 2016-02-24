# get the data points provided.
from dataIS import dataPoints, realDataPoints
from functions import *

# check the import worked
# print dataPoints[1]
# print realDataPoints[400]
# print realDataPoints[400][0]
# print realDataPoints[60][0]

data = realDataPoints

# generate coeficients
coef = [0, 0, 0, 0, 0, 0]

# calcualte fitnesses
print(getFitness(data, coef))

# sort by fitness

# get best result

# print current best coeficients



# excel coeficients
coef = [-0.006, 5000, 70, -65, 1.03, -0.00103]
print("Excel:")
print(getFitness(data, coef))

coef = [0, 1, 2, 3, 4, 5]
coef2 = [0, 1, 2, 3, 4, 5]

print(checkSameSolution(coef, coef2))