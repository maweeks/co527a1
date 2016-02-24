def checkSameSolution(coef, coef2):
    if ((coef[1] == coef2[1]) & (coef[2] == coef2[2]) & (coef[3] == coef2[3]) & (coef[4] == coef2[4]) & (coef[5] == coef2[5]) & (coef[6] == coef2[6])):
        return True
    return False

def getClosestDataPoint(data, value):
    difference = abs(value - data[0][0])
    index = 0
    for x in range(1, len(data) - 1):
        newDiff = abs(value - data[x][0])
        if newDiff < difference:
            difference = newDiff
            index = x
    return index

def getFitness(data, coef):
    fitness = 0
    for point in data:
        fitness += getSingleFitness(point, coef)
    return fitness

def getInterpolation(data, x):
    x1Index = getClosestDataPoint(data, x)
    if (data[x1Index][0] < x):
        x2Index = x1Index + 1
    else:
        x2Index = x1Index - 1

    x1 = data[x1Index][0]
    y1 = data[x1Index][1]
    x2 = data[x2Index][0]
    y2 = data[x2Index][1]

    y = y1 + (((x - x1) * (y2 - y1)) / (x2 - x1))
    return y

def getRandomCoefficient(range):
    return r
def getSingleFitness(point, coef):
    return ((getYfromX(point[0], coef) - point[1]) ** 2)

def getYfromX(x, coef):
    return (coef[1] + (coef[2] * x) + (coef[3] * (x ** 2)) + (coef[4] * (x ** 3)) + (coef[5] * (x ** 4)) + (coef[6] * (x ** 5)))

def outputCoef(coef):
    print("a: " + str(coef[1]))
    print("b: " + str(coef[2]))
    print("c: " + str(coef[3]))
    print("d: " + str(coef[4]))
    print("e: " + str(coef[5]))
    print("f: " + str(coef[6]))
    print("fit: " + str(coef[0]))

def sortByFitness(coefs):
    coefs.sort()