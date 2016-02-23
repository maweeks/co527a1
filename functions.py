def getFitness(data, a, b, c, d, e, f):
    fitness = 0
    for point in data:
        print(point)
        fitness += getSingleFitness(point, a, b, c, d, e, f)
    return fitness

def getSingleFitness(point, a, b, c, d, e, f):
    return (getYfromX(point[0], a, b, c, d, e, f) - point[1])

def getYfromX(x, a, b, c, d, e, f):
    return (a + (b * x) + (c * (x ** 2)) + (d * (x ** 3)) + (e * (x ** 4)) + (f * (x ** 5)))