import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sys

from random import sample, shuffle, random, randint
from math import floor, ceil

class Individual:
    def __init__(self, problem = None):
        if problem:
            s = [sample(["0", "1"], 1)[0] for _ in range(problem.m)]
            self.x = s
            self.size = problem.m
        else:
            self.x = []
            self.size = 0
        self.f = 0

    def fitness(self, problem):
        self.f = 0
        for i in range(1, problem.n + 1):
            for j in range(i + 1, problem.n + 1):
                for k in range(j + 1, problem.n + 1):
                    try:
                        ij = problem.edges.index((i, j))
                        ik = problem.edges.index((i, k))
                        jk = problem.edges.index((j, k))
                        if self.x[ij] == self.x[ik] and self.x[ik] == self.x[jk]: #cycle of length 3 of same color
                            self.f += 1
                    except:
                        pass

    def mutate(self, probability):
        if random() < probability:
            k = randint(0, self.size - 1)
            if self.x[k] == "1":
                self.x[k] = "0"
            else:
                self.x[k] = "1"

    @staticmethod
    def crossover(ind1, ind2, probability):
        now = Individual()
        now.x = [ind1.x[i] if random() < probability else ind2.x[i] for i in range(ind1.size)]
        now.size = ind1.size
        return now

    def printGraph(self, problem):
        G = nx.DiGraph()
        for edge in problem.edges:
            G.add_edges_from([edge])

        red_edges = [problem.edges[i] for i in range(len(problem.edges)) if self.x[i] == '0']
        edge_color = ['red' if edge in red_edges else 'blue' for edge in G.edges()]
        node_labels = {node:str(node) for node in G.nodes()}

        pos = nx.spring_layout(G)
        nx.draw_networkx_labels(G, pos, labels=node_labels)
        nx.draw(G, pos, edge_color = edge_color, node_size = 2000, node_color = 'w')

class Population:
    def __init__(self, nrInd, problem):
        self.nrInd = nrInd
        self.problem = problem
        self.arr = [Individual(problem) for _ in range(nrInd)]

    def evaluate(self):
        for individ in self.arr:
            individ.fitness(self.problem)

    def selection(self, maxInd):
        if maxInd < self.nrInd:
            self.nrInd = maxInd
            self.arr = sorted(self.arr, key = lambda Individual: Individual.f)
            self.arr = self.arr[:maxInd]

    def reunion(self, other):
        self.nrInd += other.nrInd
        self.arr = self.arr + other.arr

    def best(self, maxInd):
        arrSorted = sorted(self.arr, key = lambda Individual: Individual.f)
        return arrSorted[:maxInd]

class Problem:
    def __init__(self, fileName):
        self.n = 0
        self.m = 0
        self.vertices = []
        self.edges = []
        self.loadData(fileName)

    def loadData(self, fileName):
        print("Loading file...")
        try:
            f = open(fileName, "r")
            (self.n, self.m) = map(int, f.readline().split())
            self.vertices = map(int, f.readline().split())
            for line in f:
                (x, y) = map(int, line.split())
                if x > y:
                    (x, y) = (y, x)
                if x < 1 or x > self.n:
                    raise Exception("Corrupt file: vertex index (x)")
                if y < 1 or y > self.n:
                    raise Exception("Corrupt file: vertex index (y)")
                self.edges.append((x, y))
            print("Loaded file data: ")
            print("Number of Vertices: " + str(self.n))
            print("Number of Edges: " + str(self.m))
            if len(self.edges) != self.m:
                raise Exception("Corrupt file: number of edges")
        except Exception as e:
            print(str(e))
            sys.exit(1)

class Algorithm:
    def __init__(self, fileName, paramFileName = "param.in", nrInd = 50, nrGen = 100):
        self.problem = Problem(fileName)
        self.probability_mutate = 0.5
        self.probability_crossover = 0.5
        self.readParameters(paramFileName)
        self.nrInd = nrInd
        self.nrGen = nrGen
        self.population = Population(self.nrInd, self.problem)
        self.population.evaluate()

        self.std = []
        self.average = []
        self.bestf = []

    def readParameters(self, paramFileName):
        try:
            f = open(paramFileName, "r")
            for line in f:
                (key, value) = line.split("=")
                if key == "probability_mutate":
                    self.probability_mutate = float(value)
                elif key == "probability_crossover":
                    self.probability_crossover = float(value)
                else:
                    raise Exception("Corrupt parameters file (key)")
        except Exception as e:
            print(str(e))
            sys.exit(1)

    def iteration(self):
        parents = range(self.nrInd)
        nrChilds = len(parents) // 2
        offspring = Population(nrChilds, self.problem)
        for i in range(nrChilds):
            offspring.arr[i] = Individual.crossover(self.population.arr[i << 1], self.population.arr[(i << 1) | 1], self.probability_crossover)
            offspring.arr[i].mutate(self.probability_mutate)
        offspring.evaluate()
        self.population.reunion(offspring)
        self.population.selection(self.nrInd)

    def run(self, shouldShow = True):
        if shouldShow:
            plt.figure(num = None, figsize=(15, 7), dpi=80, facecolor='w', edgecolor='k')
        for nowIter in range(self.nrGen):
            if nowIter % 30 == 0:
                print("Running iteration: " + str(nowIter))
            self.iteration()
            if shouldShow:
                self.statistics(nowIter)
        if shouldShow:
            self.show_statistics()
        return self.population.best(10)[0]

    def statistics(self, nowIter):
        self.record_statistics(nowIter)
        plt.subplot(121)
        bst = self.population.best(1)[0]
        plt.title("Best individual\nFitness: " + str(bst.f))
        bst.printGraph(self.problem)
        self.show_statistics(nowIter, bst)

    def record_statistics(self, iteration):
        self.std.append(np.std(map(lambda Individual: Individual.f, self.population.arr)))
        self.average.append(np.average(map(lambda Individual: Individual.f, self.population.arr)))
        self.bestf.append(min(map(lambda Individual: Individual.f, self.population.arr)))

    def show_statistics(self, iteration = None, bst = None):
        plt.subplot(122)
        plt.plot(range(1, len(self.std) + 1), self.std, label = "stddev")
        plt.plot(range(1, len(self.average) + 1), self.average, label = "average")
        plt.plot(range(1, len(self.bestf) + 1), self.bestf, label = "best fitness")
        ymin = ceil(min(self.std + self.average + self.bestf)) * 2 - 1
        ymax = ceil(max(self.std + self.average + self.bestf)) * 2 + 1
        plt.ylabel("Fitness")
        plt.xlabel("Generation")
        plt.legend()
        plt.title("Statistics for generations")
        plt.axis([1, self.nrGen, ymin, ymax])
        if iteration is None:
            plt.show()
        else:
            plt.draw()
            plt.pause(0.05)
            plt.clf()

class Application:
    def __init__(self, fileName):
        self.fileName = fileName

    def main(self):
        self.algorithm = Algorithm(self.fileName)
        best = self.algorithm.run()

    def runStat(self):
        bsts = []
        for i in range(30):
            print("Running test #" + str(i))
            self.algorithm = Algorithm(self.fileName)
            bsts.append(self.algorithm.run(False))
        stddev = np.std(map(lambda Individual: Individual.f, bsts))
        average = np.average(map(lambda Individual: Individual.f, bsts))
        best = min(map(lambda Individual: Individual.f, bsts))
        print("Runned statistics for data in: " + self.fileName + "\n")
        print("Stddev: " + str(stddev))
        print("Average: " + str(average))
        print("Best: " + str(best))


app = Application("input3.in")
#app.main()
app.runStat()

