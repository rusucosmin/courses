#6. Pyramid (PSO)
#Consider n cubes of known sides length s[i] and colors c[i] . Assemble the highest
#pyramid from the cubes in such a way that it has 'stability' (there is not a bigger cube
#over a smaller one) and there are not two consecutive cubes of the same color.

from random import random, randint, shuffle
from copy import deepcopy
from math import exp
import numpy as np

W = 0.5
C1 = 0.5
C2 = 1.5

def s(v):
    return 1 / (1 + exp(-v))

class Particle:
    global W, c1, c2
    def __init__(self, n):
        self.n = n
        self.permutation = range(n)
        shuffle(self.permutation)
        self.velocity = [random() for _ in range(n)]
        self.fitness = 0
        self.bestPermutation = deepcopy(self.permutation)
        self.bestFitness = 0
        self.w = W

    def evaluate(self, problem):
        self.fitness = 1
        for i in range(1, self.n):
            if problem.s[self.permutation[i - 1]] > problem.s[self.permutation[i]] and \
                    problem.c[self.permutation[i - 1]] == problem.c[self.permutation[i]]:
                self.fitness += 1
            else:
                break
        if self.fitness > self.bestFitness:
            self.bestFitness = self.fitness
            self.bestPermutation = deepcopy(self.permutation)

    def update(self, particle, t):
        global W, C1, C2
        for i in range(self.n):
            if random() < s(self.velocity[i]):
                this = self.permutation[i]
                other = particle.permutation[i]
                for j in range(self.n):
                    if self.permutation[j] == other:
                        (self.permutation[i], self.permutation[j]) = (self.permutation[j], self.permutation[i])
            self.velocity[i] = self.w * self.velocity[i] + \
                        C1 * random() * (particle.bestPermutation[i] - self.permutation[i]) + \
                        C2 * random() * (self.bestPermutation[i] - self.permutation[i])
            self.w = W / (t + 1)

class Swarm:
    def __init__(self, swarmSize, n):
        self.v = [Particle(n) for _ in range(swarmSize)]
        self.n = swarmSize

    def getBestNeighbour(self, particle):
        return self.getBestParticles(1)[0];

    def getBestParticles(self, k):
        self.v.sort(key = lambda part: part.bestFitness)
        return self.v[-k:]

class Controller:
    def __init__(self, problem):
        self.problem = problem
        self.params = {}
        self.loadParameteres()

    def iteration(self):
        for i in range(self.params["swarmSize"]):
            current = self.swarm.v[i]
            p = self.swarm.getBestNeighbour(current)
            current.update(p, i)
            current.evaluate(self.problem)

    def showStat(self):
        fitness = []
        bestRuns = []
        for run in range(self.params["runs"]):
            print("Running %d" % (run + 1))
            bestRuns.append(self.runAlg(self.params["bestSize"]))
            runsBestParticles = map(lambda v: max(v, key = lambda s : s.bestFitness), bestRuns)
            runsBestFitness = [p.bestFitness for p in runsBestParticles]
            print("stddev: " + str(np.std(runsBestFitness)))
            print("mean: " + str(np.mean(runsBestFitness)))
            print("maxi: " + str(max(runsBestFitness)))

    def runAlg(self, topK):
        self.swarm = Swarm(self.params["swarmSize"], self.problem.n)
        for i in range(self.params["iterations"]):
            self.iteration()
        return self.swarm.getBestParticles(topK)

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
            self.n = int(f.readline())
            for line in filter(None, f.read().split('\n')):
                (x, y) = line.split(' ')
                self.s.append(x)
                self.c.append(y)
        except Exception as e:
            print("Exception Problem::loadProblem(fileName): " + str(e))

p = Problem("data02.in")
ctrl = Controller(p)
ctrl.showStat()
#for part in ctrl.runAlg(10):
#    print(str(part.bestFitness) + " " + str(part.bestPermutation))

