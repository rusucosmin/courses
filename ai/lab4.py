#6. Pyramid (PSO)
#Consider n cubes of known sides length s[i] and colors c[i] . Assemble the highest
#pyramid from the cubes in such a way that it has 'stability' (there is not a bigger cube
#over a smaller one) and there are not two consecutive cubes of the same color.

from random import random, randint
from copy import deepcopy

class Particle:
    def __init__(self, n):
        self.permutation = [randint(0, n - 1) for _ in range(n)]
        self.velocity = random()
        self.fitness = 0
        self.bestPermutation = 0
        self.bestFitness = 0

    def evaluate(self, problem):
        self.fitness = 1
        for i in range(1, n):
            if problem.s[i - 1] > problem.s[i] and problem.c[i - 1] == problem.c[i]:
                self.fitness += 1
            else:
                break
        if self.fitness > self.bestFitness:
            self.bestFitness = self.fitness
            self.bestPermutation = deepcopy(self.permutation)

    def update(self, particle):
        raise Exception("Not implemented")

class Swarm:
    def __init__(self, populationSize):
        self.v = [Particle(populationSize) for _ in range(populationSize)]
        self.n = populationSize

    def getBestNeighbour(self, particle):
        raise Exception("Not implemented")

    def getBestParticles(self):
        raise Exception("Not implemented")

class Controller:
    def __init__(self, problem):
        self.problem = problem
        self.params = {}
        self.loadParameteres()
        self.population = Swarm(self.params["initialPopulationSize"])

    def iteration(self):
        raise Exception("Not implemented")

    def runAlg(self):
        raise Exception("Not implemented")

    def loadParameteres(self):
        try:
            f = open("params.in", "r")
            for x in filter(None, f.read().split('\n')):
                (param, value) = x.split(' =')
                value = int(value)
                self.params[param] = value
        except Excepiton as e:
            print("Exception Controller::loadParameters(fileName): " + str(e))

class Problem:
    def __init__(self, fileName):
        self.s = []
        self.c = []
        self.fileName = fileName
        self.loadProblem(fileName)

    def loadProblem(self, fileName):
        try :
            f = open(fileName, "r")
            n = int(f.readline())
            for line in filter(None, f.read().split('\n')):
                (x, y) = line.split(' ')
                self.s.append(x)
                self.c.append(y)
        except Exception as e:
            print("Exception Problem::loadProblem(fileName): " + str(e))

p = Problem("data01.in")
ctrl = Controller(p)

