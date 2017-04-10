from random import sample, shuffle, random, randint


class Individual:
    def __init__(self, problem = None):
        if problem:
            s = [sample(["0", "1"], 1)[0] for _ in range(problem.m)]
            self.x = "".join(s)
            self.size = problem.m
        else:
            self.x = ""
            self.size = 0
        self.f = 0

    def fitness(self, problem):
        return 0

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

class Population:
    def __init__(self, nrInd, problem):
        self.nrInd = nrInd
        self.problem = problem
        self.arr = [Individual(problem) for _ in range(nrInd)]
        pass

    def evaluate(self):
        for individ in self.arr:
            individ.fitness()

    def selection(self):
        pass

    def reunion(self, other):
        self.nrInd += other.nrInd
        self.arr = self.arr + other.arr

class Problem:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.edges = []

    def loadData(self, fileName):
        print("Loading file...")
        f = open(fileName, "r")
        (self.n, self.m) = map(int, f.readline().split())
        for line in f:
            (x, y) = map(int, line.split())
            self.edges.append((x, y))
        print("Loaded file data: ")
        print("Number of Vertices: " + str(self.n))
        print("Number of Edges: " + str(self.m))
        print("Edges:")
        print("\n".join([str(edg) for edg in self.edges]))

class Algorithm:
    def __init__(self, nrInd = 100, nrGen = 100, fileName = "input.in"):
        self.problem = Problem()
        self.nrInd = nrInd
        self.nrGen = nrGen
        self.readParameters(fileName)
        self.population = Population(self.nrInd, self.problem)

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
        self.population = self.population.reunion(offspring)

    def run(self):
        for nowIter in range(1):
            print("Running iteration: " + str(nowIter))
            self.iteration()
            self.statistics()

    def statistics(self):
        pass

class Application:
    def __init__(self, fileName):
        self.fileName = fileName
        pass

    def main(self):
        self.algorithm = Algorithm()
        self.algorithm.run()
        pass

app = Application("input.in")
app.main()












