# get the data points provided.
from dataIS import dataPoints, realDataPoints
from functions import *
import random

# get data for plot
# use test data points
# data = dataPoints

# use the assessment data points
data = realDataPoints

# generate initial coeficients
# ----------------------------
# interpolate value for f(0) = a
a = getInterpolation(data, 0)

# interpolate value for f(1) = a + b + c + d + e + f
coefSum = getInterpolation(data, 1)
initCoef = []
for i in range(0,  1000):
    newCoef = [0, a, 0, 0, 0, 0, 0]
    coefRange = coefSum - a
    for j in range(0, 4):
        # assume the max coefficient isn't larger than 1.2 * f(1)
        newCoef[(j + 2)] = (random.random() * coefRange * 3) - (coefRange * 1.2)
        coefRange = coefRange - newCoef[(j + 2)]
    newCoef[6] = coefRange
    # calculate fitness
    newCoef[0] = (getFitness(data, newCoef))
    initCoef.append(newCoef)

# sort by fitness
sortByFitness(initCoef)
coef = initCoef[0]


# get best result
# ---------------
for i in range(0, 10000):
    x = i

# print current best coeficients
a, b, c, d, e, f = coef[1:7]
print("Best:")
outputCoef(initCoef[0])
print()
outputCoef(initCoef[1])
print()
outputCoef(initCoef[2])
print()

# calcualte fitnesses
print("F: " + str(getFitness(data, coef)))

# excel coeficients
coef = [0, -0.006, 5000, 70, -65, 1.03, -0.00103]
coef[0] = getFitness(data, coef)
print("X: " + str(coef[0]))
print("Z: 3.86877553641e+23")