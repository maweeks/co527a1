# get the data points provided.
from dataIS import dataPoints, realDataPoints
from functions import *

# a test plot
# data = dataPoints

# use the assessment data points
data = realDataPoints

# generate coeficients
# interpolate value for f(0) = a
a = getInterpolation(data, 0)

# interpolate value for f(1) = a + b + c + d + e + f
coefRange = getInterpolation(data, 1)

coef = [a, 0, 0, 0, 0, 0]

# calcualte fitnesses
print(getFitness(data, coef))

# sort by fitness

# get best result

# print current best coeficients



# excel coeficients
coef = [-0.006, 5000, 70, -65, 1.03, -0.00103]
print("Excel:")
print(getFitness(data, coef))