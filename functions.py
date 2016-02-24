def checkSameSolution(coef, coef2):
    if ((coef[0] == coef2[0]) & (coef[1] == coef2[1]) & (coef[2] == coef2[2]) & (coef[3] == coef2[3]) & (coef[4] == coef2[4]) & (coef[5] == coef2[5])):
        return True
    return False

def getFitness(data, coef):
    fitness = 0
    for point in data:
        fitness += getSingleFitness(point, coef)
    return fitness

def getSingleFitness(point, coef):
    return (((getYfromX(point[0], coef) - point[1]) ** 2) / 2)

def getYfromX(x, coef):
    return (coef[0] + (coef[1] * x) + (coef[2] * (x ** 2)) + (coef[3] * (x ** 3)) + (coef[4] * (x ** 4)) + (coef[5] * (x ** 5)))