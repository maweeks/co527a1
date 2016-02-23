# get the data points provided.
from dataIS import dataPoints, realDataPoints
from functions import *

# check the import worked
print dataPoints[1]
print realDataPoints[400]
print realDataPoints[400][0]
print realDataPoints[60][0]

data = realDataPoints

# generate coeficients
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

# calcualte fitnesses
print(getFitness(data, a, b, c, d, e, f))

# sort by fitness

# get best result

# print current best coeficients
print("q")
print(getYfromX(0, a, b, c, d, e, f))
print("w")
print(getYfromX(1, a, b, c, d, e, f))
print("e")
print(getYfromX(2, a, b, c, d, e, f))
print("r")
print(getYfromX(3, a, b, c, d, e, f))