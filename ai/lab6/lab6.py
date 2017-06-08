'''
3. Approximate the relative axial position of some tomography images based
on patient information (id, histogram of bone structure, histogram of air regions)
using a genetic programming algorithm. The set of functions will contain at least
operators +, -, *, sin, cos, and the terminal set will contain the input of the problem
and 10 constants from [0,1]. The training of the algorithm ends when the mean
square error is less than e (given as a parameter of the problem).
'''

from random import shuffle, random, randint
from numpy.random import choice
from math import floor, ceil, sin, cos
from copy import deepcopy

#with this confirutation, cost ~2.0
# parameters
TrainSIZE = 0.75  #percentage of training size
TestSIZE = 0.25   #percentage of testing size
DEPTH_MAX = 11
ITER = 100
HEADER = []
F = ['+', '-', '*']#, 'sin', 'cos']
P = [0.33, 0.33, 0.34]#, 0.02, 0.02]
#P = [0.32, 0.32, 0.32, 0.02, 0.02]
T = ["value" + str(x) for x in range(384)] + \
        ["c" + str(x) for x in range(10)]
C = [random() for _ in range(10)]

def funct(a, b):
    aux = a
    a = b
    b = aux

class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.size = 1

    def deepcopy(self):
        copy = Node()
        copy.val = self.val
        copy.size = self.size
        if self.left:
            copy.left = self.left.deepcopy()
        if self.right:
            copy.right = self.right.deepcopy()
        return copy

    def change(self, root, node1, node2):
        self.val = root.val
        if root.left:
            if root.left == node1:
                self.left = node2.deepcopy()
            else:
                self.left = Node()
                self.left.change(root.left, node1, node2)
        if root.right:
            if root.right == node1:
                self.right = node2.deepcopy()
            else:
                self.right = Node()
                self.right.change(root.right, node1, node2)
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def init(self, d):
        if d == 0:                  #terminal
            self.val = choice(T)
            return
        self.val = choice(F, p = P)
        self.left = Node()
        self.left.init(d - 1)
        self.size += self.left.size
        if self.val != 'sin' and self.val != 'cos':
            self.right = Node()
            self.right.init(d - 1)
            self.size += self.right.size

    def getNodes(self):
        ret = []
        if self.left:
            ret += self.left.getNodes()
        ret.append(self)
        if self.right:
            ret += self.right.getNodes()
        return ret

    def getNode(self, pos):
        if pos <= 0:
            assert(False)
        if pos > self.size:
            assert(False)
        if self.left and pos <= self.left.size:
            return self.left.getNode(pos)
        else:
            leftSize = 0
            if self.left:
                leftSize = self.left.size
            if leftSize + 1 == pos:
                return self
            else:
                return self.right.getNode(pos - leftSize - 1)

    def mutate(self, pos, prob):
        if pos <= 0:
            assert(False)
        if pos > self.size:
            assert(False)
        if self.left and pos <= self.left.size:
            self.left.mutate(pos, prob)
        else:
            leftSize = 0
            if self.left:
                leftSize = self.left.size
            if leftSize + 1 == pos:
                if random() < prob:
                    if self.val in T:
                        self.val = choice(T)
                    else:
                        if self.val == 'sin':
                            self.val = 'cos'
                        elif self.val == 'cos':
                            self.val = 'sin'
                        else:
                            self.val = choice(F[:3])
            else:
                self.right.mutate(pos - leftSize - 1, prob)

    def __str__(self):
        if self.val in T:
            return str(C[int(self.val[1])]) if self.val[0] == 'c' else str(self.val)
        if self.val == "sin" or self.val == "cos":
            return self.val + "(" + str(self.left) + ")"
        return str(self.left) + self.val + str(self.right)

    def __repr__(self):
        return self.__str__()

class Chromosome:
    def __init__(self, d = DEPTH_MAX):
        self.maxDepth = d
        self.fitness = 0
        self.root = Node()
        self.root.init(d)

    def evaluate(self, X, Y):
        self.fitness = 0
        exp = str(self.root)
        cnt = 0
        for (x, y) in zip(X, Y):
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            for i in range(len(x)):
                exec("{} = {}".format(HEADER[i], x[i]))
            res = eval(exp)
            self.fitness += abs(res - y)
        return self.fitness

    @staticmethod
    def crossover(ch1, ch2, prob):
        node1 = choice(ch1.root.getNodes())
        node2 = choice(ch2.root.getNodes())
        c = Chromosome()
        if ch1.root == node1:   #if we must change the whole tree
            c.root = node2.deepcopy()
        else:
            c.root = Node()
            c.root.change(ch1.root, node1, node2)
        return c

    def mutate(self, prob):
        pos = randint(1, self.root.size)
        self.root.mutate(pos, prob)

class Population:
    def __init__(self, nrInd):
        self.nrInd = nrInd
        self.arr = [Chromosome() for _ in range(nrInd)]

    def evaluate(self, X, Y):
        for ch in self.arr:
            ch.evaluate(X, Y)

    def selection(self, maxInd):
        if maxInd < self.nrInd:
            self.nrInd = maxInd
            self.arr = sorted(self.arr, key = lambda x: x.fitness)
            self.arr = self.arr[:maxInd]

    def reunion(self, other):
        self.nrInd += other.nrInd
        self.arr = self.arr + other.arr

    def best(self, maxInd):
        arrSorted = sorted(self.arr, key = lambda x: x.fitness)
        return arrSorted[:maxInd]

class GPAlgorithm:
    def __init__(self, filename, nrInd):
        self.n = 0
        self.x = []
        self.y = []
        self.xTest = []
        self.yTest = []
        self.xTrain = []
        self.yTrain = []
        self.filename = filename
        self.nrInd = nrInd
        self.pop = Population(nrInd)
        self.probability_mutate = 0.5
        self.probability_crossover = 0.5

    def iteration(self, i):
        parents = range(self.nrInd)
        nrChilds = len(parents) // 2
        offspring = Population(nrChilds)
        for i in range(nrChilds):
            offspring.arr[i] = Chromosome.crossover(self.pop.arr[i << 1], self.pop.arr[(i << 1) | 1], self.probability_crossover)
            offspring.arr[i].mutate(self.probability_mutate)
        offspring.evaluate(self.xTrain, self.yTrain)
        self.pop.reunion(offspring)
        self.pop.selection(self.nrInd)

    def run(self):
        global ITER;
        self.loadDataSet()
        self.pop.evaluate(self.xTrain, self.yTrain)
        for i in range(ITER):
            print("Iteration: " + str(i))
            self.iteration(i)
            self.pop.evaluate(self.xTrain, self.yTrain)
            self.pop.selection(self.nrInd)
            best = self.pop.best(1)[0]
            print("Best: " + str(best.root) + " " + str(best.fitness))

    def loadDataSet(self):
        global TrainSIZE, TestSIZE, HEADER
        print("Loading training data... this may take a while");
        with open(self.filename, "r") as f:
            HEADER = f.readline().split(',')[1:-1]
            for line in f.readlines()[:100]:
                values = map(float, line.split(','))
                self.x.append(values[1:-1])
                self.y.append(values[-1])
                self.n += 1
        shuffle(self.x)
        shuffle(self.y)
        self.xTrain = self.x[:int(self.n * TrainSIZE)]
        self.yTrain = self.y[:int(self.n * TrainSIZE)]
        self.xTest = self.x[int(self.n * TrainSIZE):]
        self.yTest = self.y[int(self.n * TrainSIZE):]
        print("Training size: " + str(len(self.xTrain)))
        print("Testing size: " + str(len(self.yTest)))
        assert(len(self.xTrain) + len(self.xTest) == len(self.x))
        assert(len(self.xTrain) == len(self.yTrain))
        assert(len(self.xTest) == len(self.yTest))

def __main__():
    alg = GPAlgorithm("slice_localization_data.csv", 10)
    alg.run()

__main__()
