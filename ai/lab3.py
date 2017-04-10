#for print
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

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
        if random() < 0.1:
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
        pylab.show()

class Population:
    def __init__(self, nrInd, problem):
        self.nrInd = nrInd
        self.problem = problem
        self.arr = [Individual(problem) for _ in range(nrInd)]
        pass

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
    def __init__(self):
        self.n = 0
        self.m = 0
        self.vertices = []
        self.edges = []

    def loadData(self, fileName):
        print("Loading file...")
        f = open(fileName, "r")
        (self.n, self.m) = map(int, f.readline().split())
        self.vertices = map(int, f.readline().split())
        for line in f:
            (x, y) = map(int, line.split())
            if x > y:
                (x, y) = (y, x)
            self.edges.append((x, y))
        print("Loaded file data: ")
        print("Number of Vertices: " + str(self.n))
        print("Number of Edges: " + str(self.m))
        print("Edges:")
        print("\n".join([str(edg) for edg in self.edges]))

class Algorithm:
    def __init__(self, fileName, nrInd = 100, nrGen = 10):
        self.problem = Problem()
        self.nrInd = nrInd
        self.nrGen = nrGen
        self.readParameters(fileName)
        self.population = Population(self.nrInd, self.problem)
        self.population.evaluate()

        self.std = []
        self.average = []

    def readParameters(self, fileName):
        self.problem.loadData(fileName)

    def iteration(self):
        parents = range(self.nrInd)
        nrChilds = len(parents) // 2
        offspring = Population(nrChilds, self.problem)
        for i in range(nrChilds):
            offspring.arr[i] = Individual.crossover(self.population.arr[i << 1], self.population.arr[(i << 1) | 1], 0.5)
            offspring.arr[i].mutate(0.5)
        offspring.evaluate()
        self.population.reunion(offspring)
        self.population.selection(self.nrInd)

    def run(self):
        for nowIter in range(self.nrGen):
            print("Running iteration: " + str(nowIter))
            self.iteration()
            self.record_statistics()

        self.population.best(1)[0].printGraph(self.problem)
        self.show_statistics()


        return self.population.best(10)

    def record_statistics(self):
        self.std.append(np.std(map(lambda Individual: Individual.f, self.population.arr)))
        self.average.append(np.average(map(lambda Individual: Individual.f, self.population.arr)))

    def show_statistics(self):
        plt.plot(self.std, label = "stddev")
        plt.plot(self.average, label = "average")
        plt.ylabel("fitness")
        plt.xlabel("iteration")
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
        plt.axis([0, self.nrGen, -1, 1])
        plt.show()

class Application:
    def __init__(self, fileName):
        self.fileName = fileName
        pass

    def main(self):
        self.algorithm = Algorithm(self.fileName)
        best = self.algorithm.run()
        pass

app = Application("input.in")
app.main()












