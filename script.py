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
coefSum = getInterpolation(data, 1)

coef = [a, 0, 0, 0, 0, 0]

# calcualte fitnesses
print(getFitness(data, coef))

# sort by fitness


# get best result


# print current best coeficients
a, b, c, d, e, f = coef[0:6]
print("Best:")
print("t: " + str(coefSum))
print("a: " + str(a))
print("b: " + str(b))
print("c: " + str(c))
print("d: " + str(d))
print("e: " + str(e))
print("f: " + str(f))

# calcualte fitnesses
print("F: " + str(getFitness(data, coef)))

# excel coeficients
coef = [-0.006, 5000, 70, -65, 1.03, -0.00103]
print("X: " + str(getFitness(data, coef)))